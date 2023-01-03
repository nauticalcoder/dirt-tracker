import buttons
import constants
from machine import Pin, SPI
import menu
from phew import logging
from pushbutton import Pushbutton
import queue
from services.gps import Gps
from ssd1309 import Display
from state import SystemState
import time
from uasyncio import create_task, get_event_loop, run, sleep
from xglcd_font import XglcdFont


gps = None
app_start_ticks = time.ticks_ms()
gps_queue = queue.Queue()
command_queue = queue.Queue()
system_state = SystemState()


async def render_loop(main_menu):
    while True:
        main_menu.render(system_state)
        await sleep(1)     


async def distance_loop():
    start_ticks = time.ticks_ms()
    while True:
        gps_data = await gps_queue.get()
        # Look at tim
        
        last_gps_timestamp = gps_data.timestamp
        await sleep(0.1)


def handle_button_press(button, menu):
    print(f"Button {button} pressed")
    menu.handle_input(button, buttons.COMMAND_BUTTON_ACTION_SHORTPRESS, system_state)


def handle_button_long_press(button, menu):
    print(f"Button {button} long pressed")
    menu.handle_input(button, buttons.COMMAND_BUTTON_ACTION_LONGPRESS, system_state)


async def main():
    global current_screen, loop, gps

    logging.info(f"{constants.APP_NAME} {constants.VERSION} started")
    
    gps = Gps(logging=False)
    pin21 = Pin(21, Pin.IN, Pin.PULL_DOWN)
    pin20 = Pin(20, Pin.IN, Pin.PULL_DOWN)
    button1 = Pushbutton(pin21)
    button2 = Pushbutton(pin20)
    
    # Setup display and fonts
    spi = SPI(1, baudrate=10000000, sck=Pin(10, Pin.OUT), mosi=Pin(11, Pin.OUT))
    display = Display(spi, dc=Pin(8, Pin.OUT), cs=Pin(13, Pin.OUT), rst=Pin(9, Pin.OUT))
    bally_small = XglcdFont('fonts/Bally5x8.c', 5, 8)
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    
    main_menu = menu.Menu(display, {"small": bally_small, "medium": bally, "large": unispace})

    # Setup button handlers
    button1.press_func(handle_button_press, [buttons.COMMAND_BUTTON_1, main_menu])
    button2.press_func(handle_button_press, [buttons.COMMAND_BUTTON_2, main_menu])
    button2.long_func(handle_button_long_press, [buttons.COMMAND_BUTTON_2, main_menu])
   
    # Start tasks
    
    loop = get_event_loop()
    render_task = create_task(render_loop(main_menu))
    gps_task = create_task(gps.start(gps_queue))
    loop.run_forever()
    
    #await render_task


if __name__ == '__main__':
    run(main())
