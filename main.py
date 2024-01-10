import os
from dotenv import load_dotenv
import threading
import argparse
from PyP100 import PyL530, PyP110

load_dotenv()

email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("PASSWORD")

def control_light(device_ip, on, off, delay, brightness, color_temp, color):
    l530 = PyL530.L530(device_ip, email, password)
    l530.handshake()
    l530.login()

    if on:
        if delay > 0:
            l530.turnOnWithDelay(delay)
        else:
            l530.turnOn()
    if off:
        if delay > 0:
            l530.turnOffWithDelay(delay)
        else:
            l530.turnOff()
    if brightness is not None:
        l530.setBrightness(brightness)
    if color_temp is not None:
        l530.setColorTemp(color_temp)
    if color is not None:
        l530.setColor(*color)

def control_plug(device_ip, on, off, delay):
    p110 = PyP110.P110(device_ip, email, password)
    p110.handshake()
    p110.login()

    if on:
        if delay > 0:
            p110.turnOnWithDelay(delay)
        else:
            p110.turnOn()
    if off:
        if delay > 0:
            p110.turnOffWithDelay(delay)
        else:
            p110.turnOff()

parser = argparse.ArgumentParser(description='Control TP-Link Tapo devices.')
parser.add_argument('--type', type=str, required=True, choices=['light', 'plug'], help='Type of the device')
parser.add_argument('--ip', type=str, required=True, help='IP address of the device')
parser.add_argument('--on', action='store_true', help='Turn on the device')
parser.add_argument('--off', action='store_true', help='Turn off the device')
parser.add_argument('--delay', type=int, default=0, help='Delay in seconds')
parser.add_argument('--brightness', type=int, help='Brightness for light')
parser.add_argument('--color_temp', type=int, help='Color temperature for light')
parser.add_argument('--color', type=int, nargs=2, help='Color for light')

args = parser.parse_args()

if args.type == 'light':
    thread = threading.Thread(target=control_light, args=(args.ip, args.on, args.off, args.delay, args.brightness, args.color_temp, args.color))
elif args.type == 'plug':
    thread = threading.Thread(target=control_plug, args=(args.ip, args.on, args.off, args.delay))

# start the thread
thread.start()

# wait for the thread to finish
thread.join()

