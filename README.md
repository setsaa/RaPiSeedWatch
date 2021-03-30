# RaPiSeedWatch
A program for the Raspberry Pi to monitor seed growth. It uses a Sense HAT and a camera module.

## Demo
https://youtu.be/RG9URaJmK0I

## What you'll need
* A Raspberry Pi (Keep in mind if you're using a zero you will need an extra cable for the camera module)
* A Sense HAT
* A GPIO cable or extention
* A camera module

## Setup
1. Follow the official documentation and connect the Sense HAT and the camera mod to the raspberry. Don't connect the Sense HAT directly to the RaPi, as the measurements will be affected by heat from the CPU. Use the GPIO cable for this.
2. Download this code as a zip file and transfer to your pi. Extract the file.
3. Open the terminal and type in <code>python3 </code> (include the space after).
4. Drag SeedWatch.py into the same terminal window and press `enter`.
5. Your pi will now take measurements every hour.
