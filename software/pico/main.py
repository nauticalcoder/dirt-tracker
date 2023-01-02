import buttons
from services.gps import Gps
import menu
from phew import logging
from pushbutton import Pushbutton
import queue
import time
from uasyncio import create_task, run, sleep
from xglcd_font import XglcdFont
from ssd1309 import Display
from machine import Pin, SPI
from state import SystemState

APP_NAME = "Dirt Tracker"
VERSION = "0.1"

MODE_RIDE = "ride"
MODE_CIRCUIT = "circuit"
MODE_ENDURO = "enduro"
MODE_ENDURO_TIMEKEEPING = "enduro-timekeeping"

SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

gps = None

app_start_ticks = time.ticks_ms()
gps_queue = queue.Queue()
command_queue = queue.Queue()
system_state = SystemState()

def initialize():
    global gps
    gps = Gps()
    gps.start()


async def render_loop(main_menu):
    while True:
        #if current_screen.name == SCREEN_UPLOAD_ENDURO_ROUTE:
        #    # TODO Handle transition, ideally we would encapsulate this into a state machine
        #    if previous_screen != current_screen:
        #        web_server = WebServer()
        #        web_server.start()
        #elif current_screen.name == SCREEN_MAIN:
        #    current_screen.render()
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
    global current_screen, gps
    # timer = Timer(-1)
    # timer.init(period=1000, mode=Timer.ONE_SHOT, callback=lambda t: star())
    # start_wireless_server()
    #     main_state = MainMachine()
    # setup_state_machine()

    logging.info(f"Dirty Tracker {VERSION} started")
    #initialize()
    gps = Gps(logging=False)
    pin21 = Pin(21, Pin.IN, Pin.PULL_DOWN)
    pin20 = Pin(20, Pin.IN, Pin.PULL_DOWN)
    pin19 = Pin(19, Pin.IN, Pin.PULL_DOWN)
    button1 = Pushbutton(pin21)
    button2 = Pushbutton(pin20)
    # button3 = Pushbutton(pin19)

    spi = SPI(1, baudrate=10000000, sck=Pin(10, Pin.OUT), mosi=Pin(11, Pin.OUT))
    display = Display(spi, dc=Pin(8, Pin.OUT), cs=Pin(13, Pin.OUT), rst=Pin(9, Pin.OUT))
    bally_small = XglcdFont('fonts/Bally5x8.c', 5, 8)
    bally = XglcdFont('fonts/Bally7x9.c', 7, 9)
    unispace = XglcdFont('fonts/Unispace12x24.c', 12, 24)
    main_menu = menu.Menu(display, {"small": bally_small, "medium": bally, "large": unispace})

    button1.press_func(handle_button_press, [buttons.COMMAND_BUTTON_1, main_menu])
#    button1.double_func(handle_button_1_double_press, {1})
    button2.press_func(handle_button_press, [buttons.COMMAND_BUTTON_2, main_menu])
    button2.long_func(handle_button_long_press, [buttons.COMMAND_BUTTON_2, main_menu])
#    button3.press_func(handle_button_press, {3})
   
    #while True:
    #    command = await command_queue.get()
    #    print(f"command {command}")
    #    if command:
    #        print(command)
        #print(f"Switch 1 {button21.value()}")
        #print(f"Switch 2 {sw2.value()}")
    #    await sleep(0.1)

    # print(main_menu.states.peek())
    # Start tasks
    render_task = create_task(render_loop(main_menu))
    gps_task = create_task(gps.start(gps_queue))
    
    await render_task


if __name__ == '__main__':
    run(main())
