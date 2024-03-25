## Assignment 3 Project
This assignment introduces my prototype of an electric toy car programmed to dance and move forward based on light sensor. The whole system is connected to the web server, allowing me to control the vehicle through my phone or laptop. This prototype has gone through several iterations of refinements for making the toy car run on its own without breaking down.


### Sketches:
<div style="display: flex;">
  <img src="https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/3da53d07-3d9a-4805-8d38-25fdb42ac747" alt="Car Sensor" style="width: 100%;">
  <img src="https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/442aed4d-3dba-4c2d-a0e5-d8d769b1e0a9" alt="Car Dance" style="width: 100%;">
</div>

### 'ON' State:
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
In the **_ON_** state, the vehicle moves forward as the servos move in that direction when light is detected. Servo movement stops (.move(90)) when no light is detected, indicated by a light value exceeding 40000.

### 'DANCE' State:
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
In the **_DANCE_** state, the vehicle's servos are each assigned two random values ranging from 20 to 140. Running the loop allows the servos to turn in random directions for 1/10 of a second. Resetting the servos to 90 enables them to change direction and speed, instead of continuously moving in one direction.


### Web Server & Button Control
```
# Connects to Web Server
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
```
The Wi-Fi is connected to the SSID string and password to enable the ESP32 to connect to the web server. Using HTML and CSS code, I was able to activate state changes using buttons on the web server's interface.

```
# Button to Control States
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
Buttons on the web server allow easy access to change the state of the vehicle from 'ON' to 'DANCE'. There is one caveat: the user must press the ESP32 button to turn it off in order to change the state. This is because the 'OFF' state connects the ESP32 to the web server, constantly checking the Wi-Fi and preventing any loops within the state. That is why states 'ON' and 'DANCE' cannot connect to the web server, as they require looping.

### Version 1 Prototype
![IMG_9881](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/61a48ab1-08af-49e0-91b7-58ea4b67b0b6)
The electronics did not hold very well inside the first casing of the shark car. The wheels were tilted due to the heavy center. This prototype vehicle only last for 30 seconds of running.

### Version 2 Prototype
![2nd prototype inside](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/52cefd42-2cc0-4f6f-a2eb-b5a094051f62)
![IMG_9957](https://github.com/1andreh/-SP24-IXD256-AndrewHuang/assets/158603689/ed6ead05-1b91-4520-bec1-6033b47ef874)
All electronics are now hidden. The secret method was glueing the lego connectors onto the phone to connect to the servos instead of screws. This allowed the prototype to continue running as long as there were battery in the battery pack.
