import os, sys, io
import M5
from M5 import *
from hardware import *
import time
from servo import Servo
from unit import LightUnit
import random
from unit import ToFUnit

import network
import usocket as socket

title0 = None
label0 = None
servo = None
servo1 = None
light_0 = None
i2c0 = None
tof_0 = None

program_state = 'ON'

M5.begin()

if program_state == 'OFF':
    # code to create web server and connect to wifi
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    ssid = 'ACCD'
    password = 'tink1930'

    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(ssid, password)

    print('connect to WiFi...')
    while wifi.isconnected() == False:
      print('.', end='')
      time.sleep_ms(100)

    print('WiFi connection successful')
    print(wifi.ifconfig())
    
    ip_list = wifi.ifconfig()
    ip_address = ip_list[0]
    # finished connecting to wifi


def web_page():
    global program_state
    html = """
    <html>
        <head>
            <title>Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="icon" href="data:,">
            <style>
                html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
                h1{color: #0F3376; padding: 2vh;}
                p{font-size: 1.5rem;}
                .button{display: inline-block; background-color: #e7bd3b; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
                .button2{background-color: #4286f4;}
            </style>
        </head>
        <body>
            <h1>Web Server</h1> 
            <p>program state: <strong>""" + program_state + """</strong></p>
            <p><a href="/?state=on"><button class="button">ON</button></a></p>
            <!--<p><a href="/?state=off"><button class="button button2">OFF</button></a></p>-->
            <p><a href="/?state=dance"><button class="button button2">DANCE</button></a></p>
        </body>
    </html>"""
    return html

def setup():
  global title0, label0, servo, servo1, light_0, label1, ip_address, label2
  global i2c0, tof_0
  
  i2c0 = I2C(0, scl=Pin(1), sda=Pin(2), freq=100000)
  tof_0 = ToFUnit(i2c0)

  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("ip_address", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("", 3, 25, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  label1 = Widgets.Label("", 3, 45, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  label2 = Widgets.Label("", 3, 65, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  
  servo = Servo(pin=38)
  servo.move(150)
  servo1 = Servo(pin=7)
  servo1.move(150)
  light_0 = LightUnit((1,2))
  label0.setText('1. ON')
  label1.setText('2. Dance')
  
  
  
  
def loop():
    global program_state, servo, servo1, light_0, label1, label2, i2c0, tof_0
    
    M5.update()
    if float(tof_0.get_distance()) < 8.0:
        print("DETECTED")
        # stop both servos:
#             servo.move(90)
#             servo1.move(90)
    else:
        print("NOT DETECTED")
    if program_state == 'ON':
#         if float(tof_0.get_distance()) < 8.0:
#             print("DETECTED")
#             # stop both servos:
# #             servo.move(90)
# #             servo1.move(90)
#         else:
#             print("NOT DETECTED")
            # wait for 100 milliseconds (1/10 second):
#             servo.move(85)
#             servo1.move(120)
#             time.sleep(1)
#             time.sleep_ms(100)
        label1.setText('Press to')
        label2.setText('Turn Off')
        
        # condition to exit ON state:
        if BtnA.wasPressed():
          print('button pressed!')
          program_state = 'OFF'
          label0.setColor(0xff2727, 0x000000)
          label0.setText('Status: OFF')
          print(program_state)
          label1.setText('1. ON')
          label2.setText('2. Dance')
          # stop both servos:
          servo.move(90)
          servo1.move(90)
          
    elif program_state == 'DANCE':
        # wait for 100 milliseconds (1/10 second):
        light_val = light_0.get_analog_value()
        print(light_val)
        random_num_1 = random.randint(20, 140)
        random_num_2 = random.randint(20, 140)
        for i in range(3):
          servo.move(random_num_1)
          servo1.move(random_num_2)
          time.sleep_ms(100)
          servo.move(90)
          servo1.move(90)
        # condition to exit DANCE state:
        if BtnA.wasPressed():
          print('button pressed!')
          program_state = 'OFF'
          label0.setColor(0xff2727, 0x000000)
          label0.setText('Status: OFF')
          print(program_state)
          # stop both servos:
          servo.move(90)
          servo1.move(90)
            
    elif program_state == 'OFF': # or program_state == 'DANCE':
        # code to wait for client (web page) connection
        conn, addr = s.accept()
        #state1 = 'CONNECTING'
        #state2 = 'CONNECTED'
        print('Got a connection from %s' % str(addr))
        # code for what to do after client request is received:
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        state_on = request.find('/?state=on')
        state_off = request.find('/?state=off')
        state_dance = request.find('/?state=dance')
#         label0.setText('Status: ' + program_state)
        if state_dance == 6 and state_off != 6:
          program_state = 'DANCE'
          print(program_state)
          # I want to move the robot at random
          random_num_1 = random.randint(20, 140)
          random_num_2 = random.randint(20, 140)
          servo.move(random_num_1)
          servo1.move(random_num_2)
          time.sleep_ms(100)
          servo.move(90)
          servo1.move(90)
            
            
            
#                 # Move Forward
#             servo.move(60)
#             servo1.move(80)
#             time.sleep(3)
#             servo.move(90)
#             servo1.move(90)
#                 # Move Back
#             servo.move(120)
#             servo1.move(105)
#             time.sleep(3)
#             servo.move(90)
#             servo1.move(90)
            
            
            
            
            
        if state_on == 6:
            program_state = 'ON'
            print(program_state)
            label0.setColor(0x62ff46, 0x000000)
            label0.setText('Status: ' + program_state)
            
            #led.value(1)
            #rgb.fill_color(0x0000ff)
        if state_off == 6:
            program_state = 'OFF'
            print(program_state)
            label0.setText('Status: OFF' + program_state)
            servo.move(90)
            servo1.move(90)
            time.sleep(1)
            
            
            #rgb_state = 'OFF'
            #led.value(0)
            #rgb.fill_color(0x000000)
        #print('rgb_state =', rgb_state)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
  
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













