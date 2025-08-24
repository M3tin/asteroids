import pygame
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from collectibles import Collectible


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock=pygame.time.Clock()
    dt=0

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    collectibles=pygame.sprite.Group()

    Player.containers=(updatable, drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots,updatable,drawable)
    Collectible.containers=(collectibles,drawable)

    #initialize game objects
    player=Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    afield=AsteroidField()

    while True: #game loop
        #process all events from pygame
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            
        screen.fill("black")


        
        updatable.update(dt)  #update all objects 
        
        #draw all sprites
        for obj in drawable:
            obj.draw(screen)
        
        for colb in collectibles:
            if player.check_collision(colb):
                colb.collect(player)

        for ast in asteroids:
            if player.check_collision(ast):
                player.take_damage(ast)
                    
            for bullet in shots:
                if bullet.check_collision(ast):
                    ast.split()
                    bullet.kill()
                    player.gain_score(5)
                            
        if len(collectibles.sprites())>MAX_COLLECTIBLE_ON_MAP:
            random.choice(collectibles.sprites()).kill()
        if player.lives <= 0:
            print(f"Game Over with score:{player.score}")
            return

        #last calls of the game loop
        pygame.display.flip() #refresh screen
        dt=clock.tick(60)/1000 #delta time

if __name__ == "__main__":
    main()
