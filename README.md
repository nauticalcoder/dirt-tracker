# Dirty Tracker #

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


### Inputs
Handlebar switch
We could repurpose the Checkmate switch (https://www.icoracing.com/collections/checkmate-products/products/checkmate-thumb-switch) or opt for  cheaper option like this one from Lithuania (https://www.ebay.com/itm/115052979147) or an even cheaper option like this (https://www.ebay.com/itm/184490093751?var=692193959146).

### Wheel speed sensor or GPS
We have the option of wiring up the bikes existing front wheel speed sensor or adding another sensor.  Alternatively we can add a GPS module and rely soley on GPS.  They each have their pros and cons nicely outlined in this article (https://www.icoracing.com/pages/why-gps-is-so-wrong-for-measuring-distance-travelled).


### Power
Battery or wiring into bikes electrical system.
Initially, we will rely on battery power as it is simpler and eliminates the problem of noise from the bikes electrical system.


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
### MicroPython
- Webserver with self-hosted WIFI access point - To be used for uploading configuration and route sheets
- GPS module - Read GPS module and set GPS data for access from the main application

### Known Bugs
~~- GPS read task is blocking~~

### Todo
- Add some switches to the breadboard for testing the UI
- Handle multiple screens and switching between them
- Handle executing tasks from a screen
- Add events for circuit mode: start, stop, lap
- Add background process to track distance traveled, calculate speed, lap time, avg lap time, overall time
- 

![Alt text](https://github.com/nauticalcoder/dirt-tracker/blob/master/20221219_153224.jpg "Debugging setup")

