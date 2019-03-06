#!/bin/sh 

arecord -D plughw:1,0 -d 10 /home/pi/Voice/VoiceMessage.wav
