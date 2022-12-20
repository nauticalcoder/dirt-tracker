from gps import Gps
from phew import logging
import queue
from screens.main import Main
from screens.screen import SCREEN_MAIN, SCREEN_UPLOAD_ENDURO_ROUTE
from uasyncio import create_task, run, sleep
from web_server import WebServer

from machine import Pin, Timer
import network
# from statemachine.statemachine import StateMachine, State
from state import State, StateMachine, Transition

VERSION = "0.1"

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
    
async def main():
    global current_screen, gps
    # timer = Timer(-1)
    # timer.init(period=1000, mode=Timer.ONE_SHOT, callback=lambda t: star())
    # start_wireless_server()
    #     main_state = MainMachine()
    # setup_state_machine()
    gps_queue = queue.Queue()
    
    logging.info(f"Dirty Tracker {VERSION} started")
    #initialize()
    # initialize
    gps = Gps()
    current_screen = Main()
    # Start tasks
    render_task = create_task(render_loop())
    gps_task = create_task(gps.start(gps_queue))
    
    await render_task

  

if __name__ == '__main__':
    run(main())
