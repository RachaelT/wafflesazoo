import random
import time
from rx import Observable, Observer

def five_second_timer(observer):
	while 1:
		waffles_direction = random.gauss(0, .2)
		waffles_direction = max(min(waffles_direction, 1.0), -1.0)
		observer.on_next(waffles_direction)
		#print(waffles_direction)
		time.sleep(random.randint(5.000, 10.000))

