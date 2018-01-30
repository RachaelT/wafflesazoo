import random
class WafflesPos(Observer):
	waffles_direction = 0;
	def on_next(self, x):
		waffles_direction = random.gauss(waffles_direction, 90);

	def on_error(self, e):
		print("Got error: %s" % e)

	def on_completed(self):
		print("Sequence completed")