from circleshape import *
from shot import Shot
from constants import PLAYER_SHOOT_SPEED, COLLECTIBLE_RADIUS, SCREEN_HEIGHT,SCREEN_WIDTH
import random

COLLECTIBLE_TYPES = {
    "shield":{"color":"mediumturquoise","weight":3},
    "burst":{"color":"indianred3","weight":2},
    "trap":{"color":"red","weight":1}
    }


class Collectible(CircleShape):

    def __init__(self, x, y, type):
        super().__init__(x, y, COLLECTIBLE_RADIUS)
        self.type=type
    
    def collect(self,player):
        if self.type=="shield":
            player.shield=25
        if self.type=="burst":
            angle=0
            while angle<360:
                new_shot=Shot(player.position[0],player.position[1])
                velocity=pygame.Vector2(0,1)
                velocity=velocity.rotate(angle)
                velocity=velocity*PLAYER_SHOOT_SPEED*1.3
                new_shot.velocity=velocity
                angle+=30
        if self.type=="trap":
            player.take_damage(self)
        self.kill()
    
    def draw(self,screen):
        pygame.draw.circle(screen,self.get_color(),self.position,self.radius)

    def get_color(self):
        return COLLECTIBLE_TYPES[self.type]["color"]

def spawn_collectibles():
    x=random.randint(0,SCREEN_WIDTH)
    y=random.randint(0,SCREEN_HEIGHT)
    types=[]
    weights=[]
    for t in COLLECTIBLE_TYPES.keys():
        types.append(t)
        weights.append(COLLECTIBLE_TYPES[t]["weight"])
    colb_type=random.choices(types,weights)[0]
    new_colb=Collectible(x,y,colb_type)
