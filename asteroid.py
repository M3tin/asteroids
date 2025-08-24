from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position+=self.velocity*dt
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            angle=random.uniform(20,50)
            self.velocity*=1.2
            ast1=Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            ast2=Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS)
            ast1.velocity=self.velocity.rotate(angle)
            ast2.velocity=self.velocity.rotate(-angle)
        
        
        
        self.kill()