"""
This consists of all the wrapped functions and classes to facillitate easy protyping

We recommend you to use/write any function you desire in/from this file only

Lets bring RPi to the Greek

"""
import os
import time
import socket
from RPi import GPIO

class CloudConnect(object):
  """ this connects to the cloud intended for continuos to and fro communication
  
  Args: 
  server: ip(string)
  port: port(int)
  
  """
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port
    
  
