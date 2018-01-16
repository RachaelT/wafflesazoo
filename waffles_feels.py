class WafflesFeels(Observer):
	affection = 51
	frustration = 25

 	def on_next(self, x):
 		move_goal = 
 		interrupted = 
        if(x == 123):
        	if(interrupted):

        		affection += 10
        		frustration -= 20
        	else:
        elif(x == 204):
        	if(interrupted):
        	else:

        	affection -= 1
        elif(x = 251):
        	if(interrupted):
        	else:

        	frustration += 1
        	affection -= 1
        evalFeelings()
        
    def on_error(self, e):
        print("Got error: %s" % e)
        
    def on_completed(self):
        print("Sequence completed")

    def evalFeelings():
    	if(affection < 25 and frustration < 50):
    		print("waffles is feeling lonely.")
    	if(affection > 50 and frustration < 30):
    		print("waffles is happy!")
    	if(affection > 50 and frustration > 30 ):
    		print("waffles is confused")
    	print("waffles is frustrated")
    	if(affection > 70 and frustration < 20):
    		print("waffles is in a good mood")
    	if(affection < 50 and frustration > 50):
    		print("waffles is in a bad mood")
