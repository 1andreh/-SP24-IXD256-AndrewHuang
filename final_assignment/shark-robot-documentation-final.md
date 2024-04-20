# Spaceship Shark Robot

## Introduction
After exploring servos and sensors, I wanted to learn how to build a vehicle that moves and detects objects and responds based on the object detection.
So I started sketching two different ways for the vehicle to trigger the responses.

### Sketch 1: 
![Car Sensor](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/6a924351-e02c-40b5-8df2-89248edfedfb)
I ended up following this concept of having two servoe as front wheels with a rolling backwheel to establish minimal space while achieving the vehicle to move forward, backwards, turn right, and left. I also ended up implementing the sensors, since I want the vehicle to have some sort of response when detecting an object. My first sensor I explored was the light sensor, however, I ended up using a distance sensor because there are many objects around the environment of a room, having the robot respond around the objects in the room was found to be more practical than detecting light.

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


Provide a description of your initial project idea and include images of the concept sketches that you created in Part 1 of this assignment.
Explain the reasoning behind your final choice of the project concept, whether it’s based on one of the initial sketches, a combination of or a departure from the original concepts.
