## Assignment 3 Project
This assignment introduces my prototype of an electric toy car programmed to dance and move forward based on light sensor. The whole system is connected to the web server, allowing me to control the vehicle through my phone or laptop. This prototype has gone through several iterations of refinements for making the toy car run on its own without breaking down.

### Sketches:
![Car Sensor](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/3da53d07-3d9a-4805-8d38-25fdb42ac747)
![Car Dance](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/442aed4d-3dba-4c2d-a0e5-d8d769b1e0a9)

In the state ON, the vehicle moves forward as the servos move in that direction when light is detected. Servo movement stops (.move(90)) when no light is detected - when light value exceeds 40000.
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
```

###
