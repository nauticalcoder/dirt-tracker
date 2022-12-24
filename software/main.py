from gps import Gps
from phew import logging
from pushbutton import Pushbutton
import queue
from screens.main import Main
from screens.screen import SCREEN_MAIN, SCREEN_UPLOAD_ENDURO_ROUTE
import time
from uasyncio import create_task, run, sleep
from web_server import WebServer

from machine import Pin, Timer, lightsleep
import network
# from statemachine.statemachine import StateMachine, State
from state import State, StateMachine, Transition

VERSION = "0.1"

MODE_RIDE = "ride"
MODE_CIRCUIT = "circuit"
MODE_ENDURO = "enduro"
MODE_ENDURO_TIMEKEEPING = "enduro-timekeeping"

COMMAND_BUTTON_1 = "button-one"
COMMAND_BUTTON_2 = "button-two"
COMMAND_BUTTON_3 = "button-three"
# class MainMachine(StateMachine):
#     green = State('Green', initial=True)
#     yellow = State('Yellow')
#     red = State('Red')
# 
#     slowdown = green.to(yellow)
#     stop = yellow.to(red)
#     go = red.to(green)

# main_state_machine = None
previous_screen = None
current_screen = None
gps = None
current_mode = MODE_RIDE

app_start_ticks = time.ticks_ms()
gps_queue = queue.Queue()
command_queue = queue.Queue()

def test():
    print("Test")


# def setup_state_machine():
# global main_state_machine
# main_menu = State("Main menu", initial=True)
# enduro_setup = State("Enduro setup")
# enduro_upload = State("Upload enduro route sheet")
# hare_scramble_setup = State("Hare scramble setup")
# main_state_machine = StateMachine("Main", main_menu, enduro_setup, enduro_upload, hare_scramble_setup)


def initialize():
    global gps
    gps = Gps()
    gps.start()


async def render_loop():
    while True:
        if current_screen.name == SCREEN_UPLOAD_ENDURO_ROUTE:
            # TODO Handle transition, ideally we would encapsulate this into a state machine
            if previous_screen != current_screen:
                web_server = WebServer()
                web_server.start()
        elif current_screen.name == SCREEN_MAIN:
            current_screen.render()
        await sleep(1)     


async def distance_loop():
    start_ticks = time.ticks_ms()
    while True:
        gps_data = await gps_queue.get()
        # Look at tim
        
        last_gps_timestamp = gps_data.timestamp
        await sleep(0.1)


def handle_button_press(button):
    print(f"Button {button} pressed")
    #lightsleep(10000)
    switch = {
        1: COMMAND_BUTTON_1,
        2: COMMAND_BUTTON_2,
        3: COMMAND_BUTTON_3
    }
    command_queue.put(switch.get(button))
    

def handle_button_1_double_press(button):
    print("Button {button} double pressed")


async def main():
    global current_screen, gps
    # timer = Timer(-1)
    # timer.init(period=1000, mode=Timer.ONE_SHOT, callback=lambda t: star())
    # start_wireless_server()
    #     main_state = MainMachine()
    # setup_state_machine()
  
    
    logging.info(f"Dirty Tracker {VERSION} started")
    #initialize()
    # initialize
    gps = Gps()
    current_screen = Main()
    #sw1 = Pin(28, Pin.IN, Pin.PULL_DOWN)
    pin21 = Pin(21, Pin.IN, Pin.PULL_DOWN)
    pin20 = Pin(20, Pin.IN, Pin.PULL_DOWN)
    pin19 = Pin(19, Pin.IN, Pin.PULL_DOWN)
    button1 = Pushbutton(pin21)
    button2 = Pushbutton(pin20)
    button3 = Pushbutton(pin19)

    button1.press_func(handle_button_press, {1})
    button1.double_func(handle_button_1_double_press, {1})
    button2.press_func(handle_button_press, {2})
    button3.press_func(handle_button_press, {3})

    #while True:
    #    command = await command_queue.get()
    #    print(f"command {command}")
    #    if command:
    #        print(command)
        #print(f"Switch 1 {button21.value()}")
        #print(f"Switch 2 {sw2.value()}")
    #    await sleep(0.1)
        
    # Start tasks
    render_task = create_task(render_loop())
    gps_task = create_task(gps.start(gps_queue))
    
    await render_task


if __name__ == '__main__':
    run(main())
