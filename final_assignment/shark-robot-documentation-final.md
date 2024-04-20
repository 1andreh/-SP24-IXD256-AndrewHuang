# Spaceship Shark Robot

## Introduction
After exploring servos and sensors, I wanted to learn how to build a vehicle that moves and detects objects and responds based on the object detection.
So I started sketching two different ways for the vehicle to trigger the responses.

### Sketch 1: 
![Car Sensor](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/6a924351-e02c-40b5-8df2-89248edfedfb)
I ended up following this concept of having two servoe as front wheels with a rolling backwheel to establish minimal space while achieving the vehicle to move forward, backwards, turn right, and left. I also ended up implementing the sensors, since I want the vehicle to have some sort of response when detecting an object. My first sensor I explored was the light sensor, however, I ended up using a distance sensor for my final because there are many objects around the environment of a room, having the robot respond around the objects in the room was found to be more practical than detecting light.

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

## Implementation: MVP
Video Demo: [v0.MOV.zip](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/files/15048859/v0.MOV.zip)
In order for my vehicle to move, I connected my servos and light sensors to AtomS3, using UIflow to connect the input output. I used an extension battery pack to allow the vehicle to move freely. The MVP of this vehicle has two states, to move forward, detecting light and stopping when no light has been detected and the second state allowing it to dance.

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
### Challenge Faced
Because the server needs to run the line to keep connecting, the vehicle needed to be in program_state = 'OFF' in order to change program_state to 'DANCE'

I learned how to connect the vehicle with HTTP web server, so that I can control the veihcle through my phone's web browser. Using the tutorial from Nikita, the code connects to an ip address through WIFI, printing out the ip address to connect to the vehicle. There were two CTA buttons that allowed the vehicle to change states. 


Explain your process of prototype development including all applicable aspects such as hardware (electronics), firmware (MicroPython code), software (HTML/CSS/JavaScript or other code), integrations (Adafruit IO, IFTTT, etc.), enclosure and mechanical design. Use a separate subheader for each part:
