import os
import time
from playsound import playsound # pip install playsound


# ARGS:
## 1. session : How many 20 Min sessions
## 2. Work-time-min
## 3. rest-time-sec
## 4. No-Sound
## 5. Screen-Splash


WORK_TIME_MIN = 20
REST_TIME_SEC = 20


start = time.time()

while True:
	if (time.time() - start) == WORK_TIME_MIN:
		playsound('ding.mp3')
		start_break = time.time()
		while True:
			if time.time() - start_break == REST_TIME_SEC:
				playsound('end.mp3')
				start = time.time()
				break



