#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

#button_callback 함수 정의
def button_callback(channel):
	print("button pushed!!!")

# 사용할 핀번호 정의
button_pin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Event방식 사용
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback)

while 1:
	time.sleep(0.1) 	#0.1 sec delay
