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

rgb = None
adc1 = None


def setup():
  global title0, label0, label1, label2
  global rgb, adc1

  M5.begin()
  title0 = Widgets.Title("IMU test", 3, 0x000000, 0xffffff, Widgets.FONTS.DejaVu18)
  label0 = Widgets.Label("--", 3, 20, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label1 = Widgets.Label("--", 3, 40, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  label2 = Widgets.Label("--", 3, 60, 1.0, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
  
  # initialize RGB LED strip on pin 38 with 13 pixels:
  rgb = RGB(io=38, n=13, type="SK6812")
  
  # initialize analog to digital converter on pin 1:
  adc1 = ADC(Pin(1), atten=ADC.ATTN_11DB)


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

def rgb_to_hsv(r, g, b):
  r, g, b = r/255.0, g/255.0, b/255.0
  mx = max(r, g, b)
  mn = min(r, g, b)
  df = mx-mn
  if mx == mn:
    h = 0
  elif mx == r:
    h = (60 * ((g-b)/df) + 360) % 360
  elif mx == g:
    h = (60 * ((b-r)/df) + 120) % 360
  elif mx == b:
    h = (60 * ((r-g)/df) + 240) % 360
  if mx == 0:
    s = 0
  else:
    s = (df/mx)*100
    v = mx*100
  return h, s, v

# function to combine hue, saturation, brightness into one color value:
def hsb_to_color(h, s, v):
    h = float(h)/255.0
    s = float(s)/255.0
    v = float(v)/255.0
    
    i = math.floor(h*6)
    f = h*6 - i
    p = v * (1-s)
    q = v * (1-f*s)
    t = v * (1-(1-f)*s)

    r, g, b = [
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    ][int(i%6)]
    r = int(255 * r)
    g = int(255 * g)
    b = int(255 * b)
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color

def loop():
  global title0, label0, label1, label2
  global imu_val, imu_x_val
  global rgb, adc1
  
  M5.update()
  
  # read 12-bit ADC value (0 - 4095 range):
  adc1_val = adc1.read()
  # convert ADC value to 8 bits (0 - 255 range):
  hue_val = map_value(adc1_val, in_min=0, in_max=4095, out_min=0, out_max=255)
  # show analog input on label2:
  label2.setText('adc = ' + str(hue_val))
  
  # read the IMU accelerometer values:
  imu_val = Imu.getAccel()
  
  # print all IMU values (X, Y, Z):
  print(imu_val)
  # print the first IMU value (X) only:
  #print('acc x:', imu_val[0])
  
  imu_x_val = imu_val[0]
  
  # show X-axis value:
  imu_str = 'acc x: {:0.2f}'.format(imu_x_val)
  label0.setText(imu_str)
  
  led_x = map_value(imu_x_val, -1.0, 1.0, 0, 13)
  label1.setText(str(led_x))
  
  c = hsb_to_color(hue_val, 255, 255)
  rgb.fill_color(0)  # turn off all pixels
  rgb.set_color(6, c)  # center (6th) pixel red
  # fill in pixels to the left of center:
  if led_x < 6:
    for i in range(5, led_x-1, -1):  # (start, stop, step)
      rgb.set_color(i, c)
  # fill in pixels to the right of center:
  else:
    for i in range(6, led_x):
      rgb.set_color(i, c)

#   r, g, b = hsv_to_rgb(hue_val, 255, 255)
#   rgb.set_color(led_x, get_color(r, g, b))
 
    
  #imu_str = 'acc y: {:0.2f}'.format(imu_val[1])
  #label1.setText(imu_str)
  #imu_str = 'acc z: {:0.2f}'.format(imu_val[2])
  #label2.setText(imu_str)
  
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

