from circleshape import *
from shot import Shot
from constants import SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED,PLAYER_SHOOT_COOLDOWN ,PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation=0
        self.weapon_timer=0
        self.lives=3
        self.shield=0
        self.invul=0
        self.blink=False
        self.blinktimer=0
        self.score=0
        self.text_engine=pygame.font.Font(size=36)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        self.draw_ship(screen)
        self.draw_lives(screen)
        self.draw_score(screen)
    
    def draw_score(self,screen):
        score_text=str(int(self.score))
        temp_surf=self.text_engine.render(score_text,False,"darkgoldenrod1")
        screen.blit(temp_surf,pygame.Vector2(80,100))

    def draw_lives(self, screen):
        heartpos=pygame.Vector2(50,50)
        for i in range(0,self.lives):
            heartpos[0]+=50
            pygame.draw.circle(screen,"pink",heartpos,20)

    def draw_ship(self, screen):
        if self.invul>0:
            if self.blinktimer>0:
                self.blink=not self.blink
            else:
                self.blinktimer=0.05
        else:
            self.blink=False

        if self.blink:
            return
        pygame.draw.polygon(screen,"white",self.triangle(),2)
        if self.shield:
            pygame.draw.circle(screen,"mediumturquoise",self.position,self.radius+4,1)

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
    
    def take_damage(self, other):
        if self.shield > 0:
            self.shield=0
            other.kill()
        else:
            self.lives-=1
            self.invul=1
    
    def check_collision(self, other):
        if self.invul > 0:
            return False
        return super().check_collision(other)
    
    def gain_score(self, amount):
        self.score+=amount
        
    def update(self, dt):
        self.gain_score(dt)
        keys= pygame.key.get_pressed()
        self.weapon_timer-=dt
        self.shield-=dt
        if self.shield < 0:
            self.shield=0
        if self.invul > 0:
            self.invul-=dt
            self.blinktimer-=dt

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
        
