import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self,other):
        if (self.radius+other.radius) > self.position.distance_to(other.position):
            return True
        return False
    
    def check_on_screen(self):
        return (
            self.position[0]>=0 and 
            self.position[1]>=0 and 
            self.position[0]<=SCREEN_WIDTH and
            self.position[1]<=SCREEN_HEIGHT
            )
    
    def wrap_screen(self):
        if not self.position[0]>=0:
            self.position[0]=SCREEN_WIDTH-1
        elif not self.position[0]<=SCREEN_WIDTH:
            self.position[0]=1
        elif not self.position[1]>=0:
            self.position[1]=SCREEN_HEIGHT-1
        elif not self.position[1]<=SCREEN_HEIGHT:
            self.position[1]=1
