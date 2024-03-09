# beginner program for M5Stack AtomS3 based on uiflow2 code structure

import os, sys, io
import M5
from M5 import *
from hardware import *
import time
from servo import Servo
from unit import LightUnit

import network
import usocket as socket

title0 = None
label0 = None
servo = None
servo1 = None
light_0 = None

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
    label0 = Widgets.Label("---", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
    label0.setText(ip_address)
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
        </body>
    </html>"""
    return html

def setup():
  global title0, label0, servo, servo1, light_0, label1
  
  # display title ("title text", text offset, fg color, bg color, font):
  title0 = Widgets.Title("Web Server", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  # display label ("label text", x, y, layer number, fg color, bg color, font):
  label0 = Widgets.Label("---", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  label1 = Widgets.Label("---", 3, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu12)
  
  servo = Servo(pin=38)
  servo.move(90)
  servo1 = Servo(pin=7)
  servo1.move(90)
  light_0 = LightUnit((1,2))
  
  
def loop():
    global program_state, servo, servo1, light_0, label1
    M5.update()
    if program_state == 'ON':
        # wait for 100 milliseconds (1/10 second):
        light_val = light_0.get_analog_value()
        label1.setText(str(light_val))
        print(light_val)
        if light_val < 40000:
          servo.move(65)
          servo1.move(120)
          time.sleep(1)
        elif light_val > 40000:
          servo.move(90)
          servo1.move(90)
          time.sleep(1)
        time.sleep_ms(100)
    elif program_state == 'OFF':
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
            
        if state_on == 6:
            program_state = 'ON'
            print(program_state)
            label0.setText(program_state)
            
            #led.value(1)
            #rgb.fill_color(0x0000ff)
        if state_off == 6:
            program_state = 'OFF'
            print(program_state)
            label0.setText(program_state)
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



