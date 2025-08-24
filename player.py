from circleshape import *
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED,PLAYER_SHOOT_COOLDOWN ,PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation=0
        self.weapon_timer=0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self, dt):
        self.rotation+=PLAYER_TURN_SPEED*dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot=Shot(self.position[0],self.position[1])
        velocity=pygame.Vector2(0,1)
        velocity=velocity.rotate(self.rotation)
        velocity=velocity*PLAYER_SHOOT_SPEED
        new_shot.velocity=velocity
        self.weapon_timer=PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        keys= pygame.key.get_pressed()
        self.weapon_timer-=dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE] and self.weapon_timer<=0:
            self.shoot()
