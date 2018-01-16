import random
from rx import Observable, Observer
import time

def genReport(observer):
	while True:
		
		#Generates a random speed between 0 and 255
		speed = random.randint(50, 255).to_bytes(1, byteorder='little')
		
		#Generates a random direction between 0 and 255
		direction = random.randint(0, 255).to_bytes(1, byteorder='little')
		
		#Generates a random duration between 0 and 10 seconds
		duration = random.randint(0, 10000)
		duration_bytes = duration.to_bytes(4, byteorder='little')
		
		#Generates randomly whether the move was interrupted
		interrupted = random.randint(100, 101).to_bytes(1, byteorder='little')
		

		#Reserving certain characters to indicate the type of move
		potential_moves = [123, 251, 204]
		index = random.randint(0,2)
		move_goal = potential_moves[index].to_bytes(1, byteorder='little')

		report = speed + direction + interrupted + move_goal + duration_bytes
		observer.on_next(report)
		time.sleep(duration/1000.0)

xs = Observable.create(genReport)
d = xs.subscribe(print)