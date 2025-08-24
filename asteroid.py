from circleshape import *
from constants import ASTEROID_MIN_RADIUS, ASTEROID_POINT_DEFAULT, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius, point=ASTEROID_POINT_DEFAULT):
        super().__init__(x, y, radius)
        self.point=point
        if self.point == ASTEROID_POINT_DEFAULT:
            self.color="white"
        else:
            self.color="gold3"


    def draw(self, screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius,2)

    def update(self, dt):
        self.position+=self.velocity*dt
        if not self.check_on_screen():
            if not self.color == "white":
                self.kill()
            else:
                self.wrap_screen()
    
    def split(self):
        if self.radius > ASTEROID_MIN_RADIUS:
            n_point=self.point/2
            if n_point<ASTEROID_POINT_DEFAULT:
                n_point=ASTEROID_POINT_DEFAULT
            angle=random.uniform(20,50)
            self.velocity*=1.2
            ast1=Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS,n_point)
            ast2=Asteroid(self.position[0],self.position[1],self.radius-ASTEROID_MIN_RADIUS,n_point)
            ast1.velocity=self.velocity.rotate(angle)
            ast2.velocity=self.velocity.rotate(-angle)        
        self.kill()

    def check_on_screen(self):
        return (
            self.position[0]>=-ASTEROID_MAX_RADIUS-1 and 
            self.position[1]>=-ASTEROID_MAX_RADIUS-1 and 
            self.position[0]<=SCREEN_WIDTH+ASTEROID_MAX_RADIUS+1 and
            self.position[1]<=SCREEN_HEIGHT+ASTEROID_MAX_RADIUS+1
            )