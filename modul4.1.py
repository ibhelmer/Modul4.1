#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:49:27 2019

@author: Ib Helmer Nielsen
"""
# Import all the libraries we need to run
import os
import glob
from time import sleep
#import urllib
import requests
DEBUG = 1

#Setup my API and updaterate
myAPI = "3PNCDAUDFYGHALK9"
myUpdateRate = 15 #how many seconds between posting data
#For reading DS18B20 sensor 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
   f = open(device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines

def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':
      sleep(0.2)
      lines = read_temp_raw()
   equals_pos = lines[1].find('t=')
   if equals_pos != -1:
      temp_string = lines[1][equals_pos+2:]
      temp_c = float(temp_string) / 1000.0
      return temp_c

# main() function
def main():
   
   print ('starting...')
   #Sending to data to Thingspeak
   baseURL = 'https://api.thingspeak.com/update?api_key=%s'% myAPI
   while True:
     try:
        temp = read_temp()
        req = baseURL + "&field1=%s" % temp
        print(req)
        f = requests.get(req)
        print (f.json())
        print (temp)
        sleep(int(myUpdateRate))
     except:
         print ('Error')
         break

# call main

if __name__ == '__main__':
   main()


