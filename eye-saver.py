import os
import time
from playsound import playsound # pip install playsound


WORK_TIME_MIN = 20
REST_TIME_SEC = 20


start = time.time()

while True:
	if (time.time() - start)*60 == WORK_TIME_MIN:
		playsound('ding.mp3')
		time.sleep(REST_TIME_SEC)
		playsound('end.mp3')
		start = time.time()
		



