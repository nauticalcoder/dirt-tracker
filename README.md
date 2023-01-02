# Dirty Tracker

## Hardware

### Processor
Raspberry Pi Pico W (https://www.raspberrypi.com/products/raspberry-pi-pico/)
GPS module (https://www.adafruit.com/product/746)

Pico 	
|Pico |GPS Module  | |
--- | --- | ---|
|6 - TX|RX|Using UART1 on the Pico|
|7 - RX|TX||
|36 - +3.3V|VIN||
|18 - GND|GND||


### Display
For ease if viewing, a screen with a minumum width of 4" is required but I've had trouble finding a good screen in that size.  I ordered on of these 2.42" OLED screens in white to experiment with.

https://www.aliexpress.us/item/3256802905454804.html?spm=a2g0o.new_account_index.0.0.1e3a25b9xPZlsI&gatewayAdapt=glo2usa&_randl_shipto=US

Micropython library: https://github.com/rdagger/micropython-ssd1309

### Inputs
Handlebar switch
We could repurpose the Checkmate switch (https://www.icoracing.com/collections/checkmate-products/products/checkmate-thumb-switch) or opt for  cheaper option like this one from Lithuania (https://www.ebay.com/itm/115052979147) or an even cheaper option like this (https://www.ebay.com/itm/184490093751?var=692193959146).

Added 3 buttons for command and control on the breadboard.  

### Wheel speed sensor or GPS
We have the option of wiring up the bikes existing front wheel speed sensor or adding another sensor.  Alternatively we can add a GPS module and rely soley on GPS.  They each have their pros and cons nicely outlined in this article (https://www.icoracing.com/pages/why-gps-is-so-wrong-for-measuring-distance-travelled).


### Power
Battery or wiring into bikes electrical system.
Initially, we will rely on battery power as it is simpler and eliminates the problem of noise from the bikes electrical system.
Use Pololu powerswitch to turn device on and off

### Case
Once we have all of the hardware in hand and wired up, we will design a case for it and print it using our 3d printer.



## Software
### User Interface
- Modes: 
-- Ride
--- Reset (Clear distance and time)
--- Start time
--- Stop time
-- Circuit
--- Reset (Clear distance and time)
--- Start time
--- Stop time
--- Mark lap
-- Enduro
--- 
--- 
-- Timekeeping Enduro
---
--- 
- Configuration: Setup wheel speed sensor,  Upload route sheet

### Background processes
- GPS polling
- Polling for switches
- Track distance traveled
- Render current screen
- 
### MicroPython
- Webserver with self-hosted WIFI access point - To be used for uploading configuration and route sheets
- GPS module - Read GPS module and set GPS data for access from the main application

### State Diagram
- Only fleshed out the "Ride" mode currently.  Still need to work on the more advanced "Circuit Race" and "Enduro Race" modes
- Each mode will have the following:
-- A list of informational screens that can be cycled through
-- A list of actions and the button combinations to activate them
- The main menu will be a finite state machine (FSM)
- Each mode will have its own more detailed state diagram and FSM within the application
	![Alt text](https://github.com/nauticalcoder/dirt-tracker/blob/master/Dirt%20Tracker%20State%20Diagram.svg "Debugging setup")

### Known Bugs
~~- GPS read task is blocking~~

### Todo
- Convert images to mono format and resize - Get Pillow working
- Create tiny font
- Add entry and exit transitions to main menu state machine
- ~~Add rendering of proper screen to state machine~~
- ~~Add handling of buttons to state machine~~
- ~~Add some switches to the breadboard for testing the UI~~
- ~~Define button interaction~~
- ~~Handle multiple screens and switching between them~~
- Handle executing tasks from a screen
- Add events for circuit mode: start, stop, lap
- Add background process to track distance traveled, calculate speed, lap time, avg lap time, overall time, Haversine method (https://maker.pro/forums/threads/calculating-distance-using-gps.119820/)
- Wireup breadboard so this can be tested more easily with buttons and walked outside
- ~~Wire up display~~
- Wire up webserver and wifi to Load Route screen
- 
![Alt text](https://github.com/nauticalcoder/dirt-tracker/blob/master/20221219_153224.jpg "Debugging setup")

