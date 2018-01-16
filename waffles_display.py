import pygame
import os
import time
import random
from rx import Observable, Observer


class UpdateDisplay(Observer):
	def on_next( x):
		screen.fill((255, 255, 255))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit(0)
		
		if x == "happy":
			screen.blit(pygame.transform.scale(get_image('faces/waffles_happy.png'), (400, 300)), (0, 0))
		elif x == "sad":
			screen.blit(pygame.transform.scale(get_image('faces/waffles_sad.png'), (400, 300)), (0, 0))
		elif x == "playful":
			screen.blit(pygame.transform.scale(get_image('faces/waffles_playful.png'), (400, 300)), (0, 0))
		elif x == "confused":
			screen.blit(pygame.transform.scale(get_image('faces/waffles_confused.png'), (400, 300)), (0, 0))
		elif x == "sleep":
			screen.blit(pygame.transform.scale(get_image('faces/waffles_sleep.png'), (400, 300)), (0, 0))
		else:
			screen.blit(pygame.transform.scale(get_image('faces/waffles_neutral.png'), (400, 300)), (0, 0))
		pygame.display.flip()
		



	def on_error(self, error):
		print("Got error: %s" % error)

	def on_completed(self):
		print("Sequence completed")
		


_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image



def gen_emote(observer):
	while True:

		if(pygame.mouse.get_pressed()[0] == 1):
				pygame.event.clear()
				observer.on_next("happy")
		else:
			emotions = ["sad", "playful", "confused", "sleep", ""]
			index = random.randint(0,4)
			observer.on_next(emotions[index])
		clock.tick(30)

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()


emote_gen = Observable.create(gen_emote)
disp = emote_gen.subscribe(UpdateDisplay)




