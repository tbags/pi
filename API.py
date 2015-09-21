"""
This consists of all the wrapped functions and classes to facillitate easy protyping

We recommend you to use/write any function you desire in/from this file only

Lets bring RPi to the Greek

"""
import os
import subprocess
import time
import socket
from RPi import GPIO

def arduio_upload_call(sketch, board, port):
  """
  arduino --board arduino:avr:nano:cpu=atmega168 --port /dev/ttyACM0 --upload /path/to/sketch/sketch.ino
  """
  cmd = "arduino --board %s --port %s --upload %s" % (sketch, board, port)
  a = subprocess.call(cmd, shell=True)
  return a

def init_servos(servo_pins_list, freq=100):
  """
  refer to PWM here: http://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
  p.start(dc)   # where dc is the duty cycle (0.0 <= dc <= 100.0)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(18, GPIO.OUT)
  pwm = GPIO.PWM(18, 100)
  pwm.start(5)
  """
  servo_pwm = []
  GPIO.setmode(GPIO.BCM)
  for pin in servo_pins_list:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, freq)
    pwm.start()
    servo_pwm.append(pwm)
  
  return servo_pwm
  
def servo_rotate(servo_pwm, channel, angle):
  """
  remember to enumerate approppriate channels on servo_pwm
  """
  duty = float(angle) / 10.0 + 2.5
  servo_pwm[channel].ChangeDutyCycle(duty)
  return servo_pwm

def toggle_servo(servo_pwm, channel, status=False):
  """
  only if you wish to kill the pwm or wake 
  """
  if status:
    servo_pwm[channel].start(5)
  else:
    servo_pwm[channel].stop()
  return servo_pwm
    
class CloudConnect(object):
  """ this connects to the cloud intended for continuos to and fro communication
  
  Args: 
  server: ip(string)
  port: port(int)
  
  """
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port
    
  
