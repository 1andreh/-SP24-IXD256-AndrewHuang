# Spaceship Shark Robot

## Introduction
After exploring servos and sensors, I wanted to learn how to build a vehicle that moves and detects objects and responds based on the object detection.
So I started sketching two different ways for the vehicle to trigger the responses.

### Sketch 1: 
![Car Sensor](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/6a924351-e02c-40b5-8df2-89248edfedfb)
I ended up following this concept of having two servoe as front wheels with a rolling backwheel to establish minimal space while achieving the vehicle to move forward, backwards, turn right, and left. I also ended up implementing the sensors, since I want the vehicle to have some sort of response when detecting an object. My first sensor I explored was the light sensor, however, I ended up using a distance sensor for my final because there are many objects around the environment of a room; having the robot respond around the objects in the room was found to be more practical than detecting light.

### Sketch 2: 
![Car Dance](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/7ce1c037-4a1d-41da-a4b7-354855bf3f4f)
```
if program_state == 'DANCE':
    random_num_1 = random.randint(20, 140)
    random_num_2 = random.randint(20, 140)
    for i in range(3):
      servo.move(random_num_1)
      servo1.move(random_num_2)
      time.sleep_ms(100)
      servo.move(90)
      servo1.move(90)
```
I wanted the robot to dance in a sequence because I wanted to learn how to control the robot vehicle direction. I even tested a prototype of the vehicle having servos move in random directions. I combined this direction of the robot dancing with the moving vehicle sensor by implementing two states - 1. program_state = 'DANCE' to dance, 2. program_state = 'ON' to move forward detecting light.

## Implementation
MVP Video Demo: [v0.MOV.zip](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/files/15048859/v0.MOV.zip)  
In order for my vehicle to move, I connected my servos and light sensors to AtomS3, using UIflow to connect the input output. I used an extension battery pack to allow the vehicle to move freely. The MVP of this vehicle has two states, to move forward, detecting light and stopping when no light has been detected and the second state allowing it to dance.

### Hardware
* Left Servo - moves the left wheel of the vehicle.
* Right Servo - moves the right wheel of the vehicle.
* Distance Sensor - the vehicle detects the distance of object in front of sensor, changing program states when detecting an                        object close the the sensor, chanigng the vehicle's program_state = 'BACKUP' when detecting an object 
* LED Strip - changes colors based on program state, 'ON', 'STOP', 'BACKUP'.
* M5 Battery Pack - allows the robot to become wireless and move anywhere on flat surface.
* M5 Extension - allows AtomS3 to receive four unit inputs instead of one unit.
* Rubber Tires - keeps traction for the wheels to turn the robot, preventing the vehicle to slip.

### Hardware

```
if program_state == 'OFF':
    # code to create web server and connect to wifi
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    ssid = 'WIFI_NAME'
    password = 'PASSWORD'

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
```
I learned how to connect the vehicle with HTTP web server to control the vehicle through web browser on any devices. Using the tutorial from Nikita, the code connects to an ip address through WIFI, printing out the ip address to connect to the vehicle. There were two CTA buttons that allowed the vehicle to change states. 

### HTML Web Browser
```
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
```
The web browser consists of two buttons states that control the program states of the two vehicles.

#### Challenge and Approach
```
if BtnA.wasPressed():
  print('button pressed!')
  program_state = 'OFF'
  label0.setColor(0xff2727, 0x000000)
  label0.setText('Status: OFF')
  print(program_state)
  label1.setText('1. ON')
  label2.setText('2. Dance')
  servo.move(90)
  servo1.move(90)
```
Because the server needs to run the line to keep connecting, the vehicle needed to be in program_state = 'OFF' using the AtomS3 displa button in order to press program_state to 'DANCE'. I created a display to provide steps on switching task for a good user experience.



_

Explain your process of prototype development including all applicable aspects such as hardware (electronics), firmware (MicroPython code), software (HTML/CSS/JavaScript or other code), integrations (Adafruit IO, IFTTT, etc.), enclosure and mechanical design. Use a separate subheader for each part:

Hardware

List all the separate hardware components used in your project and briefly explain what they do. To create a list with markdown syntax, use -, *, or + characters with each line of text:

item 1
item 2
etc.
Include a schematic diagram image (hand-drawn is OK) showing all the wiring connections between the M5Stack AtomS3 board and other components.

In addition, include at least one photo showing your hardware wiring. This can be several close-ups with the goal of showing how the wiring connections are made.
_

