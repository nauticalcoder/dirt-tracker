from phew import logging
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
    
#main_state_machine = None
current_menu = "upload_enduro_route"


def test():
    print("Test")
    
#def setup_state_machine():
    #global main_state_machine
    #main_menu = State("Main menu", initial=True)
    #enduro_setup = State("Enduro setup")
    #enduro_upload = State("Upload enduro route sheet")
    #hare_scramble_setup = State("Hare scramble setup")
    #main_state_machine = StateMachine("Main", main_menu, enduro_setup, enduro_upload, hare_scramble_setup)
    
def main():
    #timer = Timer(-1)
    #timer.init(period=1000, mode=Timer.ONE_SHOT, callback=lambda t: star())
    #start_wireless_server()
#     main_state = MainMachine()
    #setup_state_machine()
    logging.info(f"Dirty Tracker {VERSION} started")
    if current_menu == "upload_enduro_route":
        web_server = WebServer()
        web_server.start()
            
        
if __name__ == '__main__':
    main()
