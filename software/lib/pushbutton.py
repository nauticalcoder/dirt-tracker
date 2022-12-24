# pushbutton.py

# Copyright (c) 2018-2022 Peter Hinch
# Released under the MIT License (MIT) - see LICENSE file

import uasyncio as asyncio
import utime as time
from utime import ticks_add, ticks_diff, ticks_ms

try:
    from machine import TouchPad
except ImportError:
    pass

async def _g():
    pass
type_coro = type(_g())

# If a callback is passed, run it and return.
# If a coro is passed initiate it and return.
# coros are passed by name i.e. not using function call syntax.
def launch(func, tup_args):
    res = func(*tup_args)
    if isinstance(res, type_coro):
        res = asyncio.create_task(res)
    return res

class Pushbutton:
    debounce_ms = 50
    long_press_ms = 1000
    double_click_ms = 400

    def __init__(self, pin, suppress=False, sense=None):
        self._pin = pin  # Initialise for input
        self._supp = suppress
        self._dblpend = False  # Doubleclick waiting for 2nd click
        self._dblran = False  # Doubleclick executed user function
        self._tf = False
        self._ff = False
        self._df = False
        self._ld = False  # Delay_ms instance for long press
        self._dd = False  # Ditto for doubleclick
        # Convert from electrical to logical value
        self._sense = pin.value() if sense is None else sense
        self._state = self.rawstate()  # Initial state
        self._run = asyncio.create_task(self._go())  # Thread runs forever

    async def _go(self):
        while True:
            self._check(self.rawstate())
            # Ignore state changes until switch has settled. Also avoid hogging CPU.
            # See https://github.com/peterhinch/micropython-async/issues/69
            await asyncio.sleep_ms(Pushbutton.debounce_ms)

    def _check(self, state):
        if state == self._state:
            return
        # State has changed: act on it now.
        self._state = state
        if state:  # Button pressed: launch pressed func
            if self._tf:
                launch(self._tf, self._ta)
            if self._ld:  # There's a long func: start long press delay
                self._ld.trigger(Pushbutton.long_press_ms)
            if self._df:
                if self._dd():  # Second click: timer running
                    self._dd.stop()
                    self._dblpend = False
                    self._dblran = True  # Prevent suppressed launch on release
                    launch(self._df, self._da)
                else:
                    # First click: start doubleclick timer
                    self._dd.trigger(Pushbutton.double_click_ms)
                    self._dblpend = True  # Prevent suppressed launch on release
        else:  # Button release. Is there a release func?
            if self._ff:
                if self._supp:
                    d = self._ld
                    # If long delay exists, is running and doubleclick status is OK
                    if not self._dblpend and not self._dblran:
                        if (d and d()) or not d:
                            launch(self._ff, self._fa)
                else:
                    launch(self._ff, self._fa)
            if self._ld:
                self._ld.stop()  # Avoid interpreting a second click as a long push
            self._dblran = False

    def _ddto(self):  # Doubleclick timeout: no doubleclick occurred
        self._dblpend = False
        if self._supp and not self._state:
            if not self._ld or (self._ld and not self._ld()):
                launch(self._ff, self._fa)

    # ****** API ******
    def press_func(self, func=False, args=()):
        if func is None:
            self.press = asyncio.Event()
        self._tf = self.press.set if func is None else func
        self._ta = args

    def release_func(self, func=False, args=()):
        if func is None:
            self.release = asyncio.Event()
        self._ff = self.release.set if func is None else func
        self._fa = args

    def double_func(self, func=False, args=()):
        if func is None:
            self.double = asyncio.Event()
            func = self.double.set
        self._df = func
        self._da = args
        if func:  # If double timer already in place, leave it
            if not self._dd:
                self._dd = Delay_ms(self._ddto)
        else:
            self._dd = False  # Clearing down double func

    def long_func(self, func=False, args=()):
        if func is None:
            self.long = asyncio.Event()
            func = self.long.set
        if func:
            if self._ld:
                self._ld.callback(func, args)
            else:
                self._ld = Delay_ms(func, args)
        else:
            self._ld = False

    # Current non-debounced logical button state: True == pressed
    def rawstate(self):
        return bool(self._pin() ^ self._sense)

    # Current debounced state of button (True == pressed)
    def __call__(self):
        return self._state

    def deinit(self):
        self._run.cancel()


# delay_ms.py Now uses ThreadSafeFlag and has extra .wait() API
# Usage:
# from primitives import Delay_ms

# Copyright (c) 2018-2022 Peter Hinch
# Released under the MIT License (MIT) - see LICENSE file


class Delay_ms:

    class DummyTimer:  # Stand-in for the timer class. Can be cancelled.
        def cancel(self):
            pass
    _fake = DummyTimer()

    def __init__(self, func=None, args=(), duration=1000):
        self._func = func
        self._args = args
        self._durn = duration  # Default duration
        self._retn = None  # Return value of launched callable
        self._tend = None  # Stop time (absolute ms).
        self._busy = False
        self._trig = asyncio.ThreadSafeFlag()
        self._tout = asyncio.Event()  # Timeout event
        self.wait = self._tout.wait  # Allow: await wait_ms.wait()
        self.clear = self._tout.clear
        self.set = self._tout.set
        self._ttask = self._fake  # Timer task
        self._mtask = asyncio.create_task(self._run()) #Main task

    async def _run(self):
        while True:
            await self._trig.wait()  # Await a trigger
            self._ttask.cancel()  # Cancel and replace
            await asyncio.sleep_ms(0)
            dt = max(ticks_diff(self._tend, ticks_ms()), 0)  # Beware already elapsed.
            self._ttask = asyncio.create_task(self._timer(dt))

    async def _timer(self, dt):
        await asyncio.sleep_ms(dt)
        self._tout.set()  # Only gets here if not cancelled.
        self._busy = False
        if self._func is not None:
            self._retn = launch(self._func, self._args)

# API
    # trigger may be called from hard ISR.
    def trigger(self, duration=0):  # Update absolute end time, 0-> ctor default
        if self._mtask is None:
            raise RuntimeError("Delay_ms.deinit() has run.")
        self._tend = ticks_add(ticks_ms(), duration if duration > 0 else self._durn)
        self._retn = None  # Default in case cancelled.
        self._busy = True
        self._trig.set()

    def stop(self):
        self._ttask.cancel()
        self._ttask = self._fake
        self._busy = False
        self._tout.clear()

    def __call__(self):  # Current running status
        return self._busy

    running = __call__

    def rvalue(self):
        return self._retn

    def callback(self, func=None, args=()):
        self._func = func
        self._args = args

    def deinit(self):
        self.stop()
        self._mtask.cancel()
        self._mtask = None


class ESP32Touch(Pushbutton):
    thresh = (80 << 8) // 100

    @classmethod
    def threshold(cls, val):
        if not (isinstance(val, int) and 0 < val < 100):
            raise ValueError("Threshold must be in range 1-99")
        cls.thresh = (val << 8) // 100

    def __init__(self, pin, suppress=False):
        self._thresh = 0  # Detection threshold
        self._rawval = 0
        try:
            self._pad = TouchPad(pin)
        except ValueError:
            raise ValueError(pin)  # Let's have a bit of information :)
        super().__init__(pin, suppress, False)

    # Current logical button state: True == touched
    def rawstate(self):
        rv = self._pad.read()  # ~220μs
        if rv > self._rawval:  # Either initialisation or pad was touched
            self._rawval = rv  # when initialised and has now been released
            self._thresh = (rv * ESP32Touch.thresh) >> 8
            return False  # Untouched
        return rv < self._thresh