import pygame

kirby = pygame.transform.scale(pygame.image.load("Kirby_Standing.png"), (100,90))
k_hitbox = kirby.get_rect()
kirby_fly = pygame.transform.scale(pygame.image.load("kirbyflight.png"), (100,90))
kirby_inhale_1 = pygame.transform.scale(pygame.image.load("kirbyinhale1.png"), (100,90))
kirby_inhale_2 = pygame.transform.scale(pygame.image.load("kirbyinhale2.png"), (100,90))
vacuum = pygame.rect.Rect(0,0,300,110)
kirby_frame = kirby
inhale_start = pygame.mixer.Sound("inhaleStart.wav")
inhale_continue = pygame.mixer.Sound("inhaleContinue.wav")
p_x = 400
p_y = 50
p_xspeed = 0
p_yspeed = 0
width = 1440
height = 900
ground = (width//4-100,height//2, width//4+800,height//2)


class Kirb:
    def __init__(self):
        self.hitbox = k_hitbox
        self.image = {"idle":kirby, "flight":kirby_fly, "inhale1":kirby_inhale_1, "inhale2":kirby_inhale_2}
        self.x = p_x
        self.y = p_y
        self.dx = p_xspeed
        self.dy = p_yspeed
        self.facing_left = False
        self.grounded = False
        self.inhale = False
        self.score = 0
        self.inhale_time = 0
        self.frame = self.image["idle"]
        self.munch_space = vacuum
    def moving(self):
        keys_pressed = pygame.key.get_pressed()
        
        if keys_pressed[pygame.K_SPACE] and self.grounded:
           
            self.inhale = True
            self.dx = 0
            self.y = (height//2-1)
            if self.inhale and self.frame == self.image["inhale2"]:
                if keys_pressed[pygame.K_a]:
                    self.facing_left = True
                print(self.facing_left)
                if self.facing_left:
                    self.munch_space.x = self.x+70
                else:
                    self.munch_space.x = self.x-330 
                self.munch_space.y = self.y-100
        else:
            self.inhale = False
        if keys_pressed[pygame.K_a] and not self.inhale:
            self.facing_left = True
            self.dx = max(self.dx - 1, -8)
        elif keys_pressed[pygame.K_d] and not self.inhale:
            self.facing_left = False
            self.dx = min(self.dx + 1, +8)
        else:
            self.dx *=.8
        self.x+=self.dx

        if keys_pressed[pygame.K_w] and self.grounded and not self.inhale:
            self.dy = -30
        elif self.grounded:
            self.dy = 0
        else:
            self.dy = min(self.dy+2, 20)
        self.y+=self.dy
        self.hitbox.x = self.x
        self.hitbox.y = self.y

        if self.hitbox.clipline(ground):
            self.grounded = True
            while self.hitbox.bottom > ground[1] +.1:
                self.y-=1
                self.hitbox.y = self.y
        else:
            self.grounded = False
        
        if self.hitbox.y>900:
            self.y = 0
            self.x = 700
            self.score-= 20
    def animation(self):
        if self.inhale:
            self.inhale_time+=1
            if self.inhale_time < 20:
                if inhale_start.get_num_channels() < 1:
                    inhale_start.play()
                self.frame = self.image["inhale1"]
                if self.facing_left:
                    self.frame = pygame.transform.flip(self.frame, self.facing_left, False)
            else:
                inhale_start.stop()
                if inhale_continue.get_num_channels() < 1:
                    inhale_continue.play()
                self.frame = self.image["inhale2"]
                if self.facing_left:
                    self.frame = pygame.transform.flip(self.frame, self.facing_left, False)
        else:
            self.inhale_time = 0
        if self.grounded is False and self.dy != 0:
            self.frame = self.image["flight"]
            if self.facing_left:
                self.frame = pygame.transform.flip(self.frame, self.facing_left, False)
        if self.grounded and not self.inhale:
            self.frame = self.image['''''''idle']
            if self.facing_left:
                self.frame = pygame.transform.flip(self.frame, self.facing_left, False)
    def update(self, screen):
        self.moving()
        self.animation()
        screen.blit(self.frame,self.hitbox)
        pygame.draw.rect(screen, (0,0,0), self.munch_space)