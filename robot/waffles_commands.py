class WafflesCMD(Observer):
	affection = 0
	frustration = 0
	def on_next(self, x):
		if(EMOTION_UPDATE_TYPE):
			#Update emotions, send emotional movement command
		elif(BEING PETTED):
			#stop everything
			#when no longer petted, emotional behavior,  then back to normal
		else:
			#randomly send emotional movement command, small percent of time
			#interpret direction
		

	def on_error(self, e):
		print("Got error: %s" % e)

	def on_completed(self):
		print("Sequence completed")


	#big dictionary of emotive movements