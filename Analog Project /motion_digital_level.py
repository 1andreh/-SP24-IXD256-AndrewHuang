import os, sys, io
import M5
from M5 import *
from hardware import *
import time
import math

title0 = None
label0 = None
label1 = None
label2 = None

imu_val = None
imu_x_val = 0.0
imu_x_last = 0.0

rgb = None

update_timer = 0
motion_timer = 0
program_state = 'IDLE'


def setup():
    global title0, label0, label1, label2
    global rgb

    M5.begin()
    title0 = Widgets.Title("IMU test", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
    label1 = Widgets.Label("", 50, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
    label2 = Widgets.Label("--", 3, 60, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)

    # initialize RGB LED strip on pin 38 with 13 pixels:
    rgb = RGB(io=2, n=13, type="SK6812")


# function to map input value range to output value range:
def map_value(in_val, in_min, in_max, out_min, out_max):
    out_val = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if out_val < out_min:
        out_val = out_min
    elif out_val > out_max:
        out_val = out_max
    return int(out_val)


def get_color(r, g, b):
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color


def loop():
    global title0, label0, label1, label2
    global imu_val, imu_x_val, imu_x_last, rgb
    global motion_timer, update_timer, program_state

    M5.update()

    # read the IMU accelerometer values:
    imu_val = Imu.getAccel()

    # print all IMU values (X, Y, Z):
    print(imu_val)
    # print the first IMU value (X) only:
    # print('acc x:', imu_val[0])
    imu_x_last = imu_x_val  # save the last imu_y_val
    imu_x_val = imu_val[0]

    # show X-axis value:
    # imu_str = 'acc x: {:0.2f}'.format(imu_x_val)
    # label0.setText(imu_str)

    # I want to display a green right arrow & left red arrow when tilted.
    # I want to change color to green when detecting motion
    # Y-axis acceleration difference (absolute value):
    imu_x_diff = imu_x_val - imu_x_last

    if program_state == 'IDLE':
        # change from IDLE to MOTION state when motion is detected:
        if imu_x_diff > 0.25 or imu_x_diff < -0.25:
            program_state = 'MOTION'
            # reset motion timer:
            motion_timer = time.ticks_ms()
    elif program_state == 'MOTION':
        # change back to IDLE state 3 seconds after motion was detected:
        if (time.ticks_ms() > motion_timer + 3000):
            program_state = 'IDLE'

    # maps the led to the value of the tilted degree
    led_x = map_value(imu_x_val, -1.0, 1.0, 0, 13)
    label1.setText(str(led_x))

    deg_x = map_value(imu_x_val, -1.0, 1.0, -90, 90)
    label1.setText(str(deg_x))

    rgb.fill_color(0)  # turn off all pixels
    rgb.set_color(6, get_color(255, 0, 0))  # center (6th) pixel red

    # fill in pixels to the left of center:
    if led_x < 6:
        for i in range(5, led_x - 1, -1):  # (start, stop, step)
            rgb.set_color(i, get_color(255, 0, 0))
            if program_state == 'MOTION':
                rgb.set_color(i, get_color(0, 255, 0))
    # fill in pixels to the right of center:
    else:
        for i in range(6, led_x):
            rgb.set_color(i, get_color(255, 0, 0))
            if program_state == 'MOTION':
                rgb.set_color(i, get_color(0, 255, 0))

    # Now i is defined properly and can be used here
    if program_state == 'MOTION':
        rgb.set_color(led_x, get_color(0, 255, 0))
    else:
        rgb.set_color(led_x, get_color(255, 0, 0))

    label2.setText(program_state)

    time.sleep_ms(100)


if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("please update to latest firmware")

