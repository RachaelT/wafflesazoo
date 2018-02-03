import pygame 
from os import sys

def waffles_feels(observer):
    SAD_WAFFLES = pygame.USEREVENT + 1
    SLEEP_WAFFLES = pygame.USEREVENT + 2

    was_pet = False
    while True:
        #true when waffles is being petted
        if(pygame.mouse.get_pressed()[0] == 1):
                pygame.time.set_timer(SAD_WAFFLES, 6000)
                if not was_pet:
                    observer.on_next("happy")
                    pygame.time.set_timer(SLEEP_WAFFLES, 3000)
                    was_pet = True

        #Randomly generates emotions
        else:
            if was_pet:
                was_pet = False
                observer.on_next("neutral")
            pygame.time.set_timer(SLEEP_WAFFLES, 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == SAD_WAFFLES:
                observer.on_next("sad")
            elif event.type == SLEEP_WAFFLES:
                observer.on_next("sleep")


    clock.tick(30)