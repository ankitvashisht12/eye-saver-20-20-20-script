import os
import time
from playsound import playsound # pip install playsound


WORK_TIME_MIN = 20.0
REST_TIME_SEC = 30.0


start = time.time()

while True:
	if (time.time() - start)/60 == WORK_TIME_MIN:
		playsound( os.path.join('sounds', 'ding.mp3'))
		time.sleep(REST_TIME_SEC)
		playsound( os.path.join('sounds', 'end.mp3'))
		start = time.time()
		



