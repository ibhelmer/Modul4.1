#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:00:57 2019

@author: Ib Helmer Nielsen
"""

# Import all the libraries we need to run
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import urllib2



DEBUG = 1
# Setup the pins we are connect to
RCpin = 24
DHTpin = 23

#Setup our API and delay
myAPI = "***Insert Your API CODE HERE***"
myDelay = 15 #how many seconds between posting data

GPIO.setmode(GPIO.BCM)
GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def getSensorData():  
    
    # return dict
    return (str(RHW), str(TW),str(TWF))

    
# main() function
def main():
    
    print 'starting...'

    baseURL """
