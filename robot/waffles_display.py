import pygame
import os
import time
import random
import requests
from rx import Observable, Observer
from waffles_feels import waffles_feels
from waffles_commands import WafflesCMD

ser = serial.Serial('/dev/ttyAMA0')

#Updates the actual displayed image based on waffle's reported emotional state.
class UpdateDisplay(Observer):
	def on_next(x):
		screen.fill((255, 255, 255))

		#Quits when the screen is closed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit(0)

		#Loads the appropriate image for the emotion
		screen.blit(pygame.transform.scale(get_image('../faces/waffles_' + x + '.png'), (400, 300)), (0, 0))

		#Updates the website with the new image
		requests.post("http://wafflesazoo.mit.edu/set_mood", json=x)
		pygame.display.flip()

	def on_error(error):
		print("Got error: %s" % error)

	def on_completed(self):
		print("Sequence completed")
		
#Helper method for retrieving images
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image


#starting the display
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

CMD = WafflesCMD()

#Creates an observable that publishes the same stream to multiple observers
emote_gen = Observable.create(waffles_feels).publish()

#The display subscriber
disp = emote_gen.subscribe(UpdateDisplay)

#The serial communication subscriber
cmd = emote_gen.subscribe(CMD)

emote_gen.connect()



