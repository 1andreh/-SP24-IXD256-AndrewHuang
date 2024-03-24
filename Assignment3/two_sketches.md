## Assignment 3 Project
This assignment introduces my prototype of an electric toy car programmed to dance and move forward based on light sensor. The whole system is connected to the web server, allowing me to control the vehicle through my phone or laptop. This prototype has gone through several iterations of refinements for making the toy car run on its own without breaking down.

### Sketches:
<div style="display: flex;">
  <img src="https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/3da53d07-3d9a-4805-8d38-25fdb42ac747" alt="Car Sensor" style="width: 50%;">
  <img src="https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/442aed4d-3dba-4c2d-a0e5-d8d769b1e0a9" alt="Car Dance" style="width: 50%;">
</div>

### On State:
```
if program_state == 'ON':
    # wait for 100 milliseconds (1/10 second):
    light_val = light_0.get_analog_value()
    print(light_val)
    rand_int = random.randint(40, 65)
    if light_val < 40000:
        servo.move(70)
        servo1.move(110)
    elif light_val > 40000:
        servo.move(90)
        servo1.move(90)
        time.sleep(1)
    time.sleep_ms(100)
```
In the state **_ON_**, the vehicle moves forward as the servos move in that direction when light is detected. Servo movement stops (.move(90)) when no light is detected - when light value exceeds 40000.

### Dance State:
```
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
```
In the state of **_DANCE_**, the vehicle's servos are each mapped with two random values ranging from 20-140. Running the loop will allow the servoes to turn at random directions for 1/10 of a second. Setting the servos back to 90 will allow the servos change direction and speed, instead of moving in one direction perpetually.

### Web Server & Button Control
```
if BtnA.wasPressed():
    print('button pressed!')
    program_state = 'OFF'
    label0.setColor(0xff2727, 0x000000)
    label0.setText('Status: OFF')
    print(program_state)
    # stop both servos:
    servo.move(90)
    servo1.move(90)
```
