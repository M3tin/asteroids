import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock=pygame.time.Clock()
    dt=0

    player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True: #game loop
        #process all events from pygame
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            
        screen.fill("black")


        #update all objects
        player.update(dt)

        #draw sprites
        player.draw(screen)        

        #last calls of the game loop
        pygame.display.flip() #refresh screen
        dt=clock.tick(60)/1000 #delta time

if __name__ == "__main__":
    main()
