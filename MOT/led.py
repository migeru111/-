#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import subprocess
#!/Usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime
import smtplib
import mimetypes
import imghdr
import sndhdr

from argparse import ArgumentParser
from email.message import EmailMessage
from email.policy import SMTP

def switch_on(channel):

#cmd_red="/home/pi/Voice/VoiceMessage.sh"
#green_path="~/Mot/GreenMail.py"
#yellow_path="~/Mot/YellowMail.py"

  if(channel == 21):
       GPIO.output(15,GPIO.HIGH) # good_condition
       print("power on green")
       subprocess.call("python3 good_mail.py",shell=True)
       #subprocess.call("/home/pi/Voice/VoiceMessage.sh",shell=True)


  if(channel == 20):
       GPIO.output(15,GPIO.HIGH) # boicemessage
       print("power on red")
       #subprocess.call(cmd_red,shell=True)
       subprocess.call("/home/pi/Voice/VoiceMessage.sh",shell=True)
       subprocess.call("python3 Voice_mail.py",shell=True)


  if(channel == 16):
       GPIO.output(15,GPIO.HIGH) # bad_condition
       print("power on yellow")
       subprocess.call("python3 bad_mail.py",shell=True)
       #subprocess.call("/home/pi/Voice/VoiceMessage.sh",shell=True)


GPIO.setmode(GPIO.BCM)  # 初期設定
#GPIO.cleanup() # GPIO初期化
GPIO.setup(15,GPIO.OUT) # 出力設定
# GPIO.setup(26,GPIO.OUT)  # 入力設定
#GPIO.setup(19,GPIO.IN) # 出力設定
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # 入力設定
GPIO.add_event_detect(21,GPIO.RISING,callback=switch_on,bouncetime=3000)
GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # 入力設定
GPIO.add_event_detect(20,GPIO.RISING,callback=switch_on,bouncetime=11000)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)  # 入力設定
GPIO.add_event_detect(16,GPIO.RISING,callback=switch_on,bouncetime=3000)
# タクトスイッチの状態をもとに判定する
# 押す=HIGH はなす=LOW

try:
    while True:
         GPIO.output(15,GPIO.LOW) # LED点灯
         sleep(0.01)

except KeyboardInterrupt:
    pass



GPIO.cleanup() # GPIO初期化
#GPIO.output(15,GPIO.LOW)  # LED消灯
