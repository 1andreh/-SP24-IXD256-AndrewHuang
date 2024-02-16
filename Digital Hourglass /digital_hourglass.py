import os, sys, io
from M5 import *
from hardware import *
import random
import time

# Initial global variables setup
title0 = None
pin1 = None
pin41 = None
blue_circles_count = 0
blue_circles_threshold = 4000  # Number of blue circles
time_up_displayed = False
rgb2 = None
gen_time = 1  # Start with slow generation time
i = None
is_fast_mode = False  # Flag to track if we're in fast mode

def setup():
    global title0, pin1, rgb2, pin41
    M5.begin()
    title0 = Widgets.Title("Hello AtomS3", 3, 0xFFFFFF, 0x0e0e0e, Widgets.FONTS.DejaVu12)
    title0.setText('button input')
    pin1 = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)
    rgb2 = RGB(io=38, n=10, type="SK6812")
    pin41 = Pin(41, mode=Pin.IN)

def draw_time_up_message():
    global rgb2
    M5.Lcd.setTextSize(2)
    M5.Lcd.setTextColor(0x000000, 0xFFFFFF)
    M5.Lcd.setCursor(40, 80)
    M5.Lcd.print('Time is up!')

def generate_random_blue_color():
    r = random.randint(0, 50)
    g = random.randint(0, 50)
    b = random.randint(150, 255)
    return (r << 16) | (g << 8) | b

def reset_display():
    global blue_circles_count, time_up_displayed
    title0.setText('Resetting')
    time.sleep(0.5)
    M5.Lcd.fillScreen(0x000000)
    title0.setText('button input')
    blue_circles_count = 0
    time_up_displayed = False

def toggle_speed():
    global is_fast_mode, gen_time, title0
    is_fast_mode = not is_fast_mode  # Toggle the speed mode
    if is_fast_mode:
        gen_time = 0.5
        title0 = Widgets.Title("Read Mode", 3, 0x00FFFF, 0x0e0e0e, Widgets.FONTS.DejaVu12)
    else:
        gen_time = 2
        title0 = Widgets.Title("Read Mode", 3, 0xFFFFFF, 0x0e0e0e, Widgets.FONTS.DejaVu12)
    

def loop():
    global title0, pin1, blue_circles_count, time_up_displayed, gen_time, is_fast_mode
    connect_val = pin1.value()
    M5.update()
    button_pressed = BtnA.isPressed()  # Check if button was pressed since last loop

    if button_pressed:
        toggle_speed()  # Toggle between fast and slow generation times
        time.sleep_ms(50)

    if not time_up_displayed and connect_val == 0:
        x = random.randint(0, M5.Lcd.width() - 1)
        y = random.randint(0, M5.Lcd.height() - 1)
        radius = random.randint(1, 4)
        random_color = generate_random_blue_color()
        M5.Lcd.fillCircle(x, y, radius, random_color)
        title0.setText('Read Mode') 
        time.sleep(gen_time)  # Use the current generation time
        blue_circles_count += 1

        if blue_circles_count >= blue_circles_threshold:
            draw_time_up_message()
            time_up_displayed = True
            time.sleep(2)

    elif time_up_displayed and connect_val == 0:
        title0.setText('Resting')
    elif connect_val != 0:
        title0.setText('Resting')

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        print("Error:", e)

