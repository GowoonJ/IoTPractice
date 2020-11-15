#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 사용할 핀번호 정의
button_pin=15
led_pin=4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#버튼 핀 INPUT 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#LED핀 OUT 설정
GPIO.setup(led_pin, GPIO.OUT)

light_on=False

# define button_callback fun
def button_callback(channel):
	global light_on
	if light_on == False:
		GPIO.output(led_pin,1)
		print("LED ON!!!!")
	else:
		GPIO.output(led_pin,0)
		print("LED OFFFF!!")
	light_on = not light_on
	
#Event 알림 방식으로 신호 감지 시 button_callback 함수 실행,
#300ms 바운스 타임 설정 잘못된 신호 방지
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback,bouncetime=300)

while 1:
	time.sleep(0.1)
