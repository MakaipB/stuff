import pygame
import random

class Fruit():
    def __init__(self):
        self.points = 0
        self.image = None
        self.active = False
        self.zone = None
        self.x = 0
        self.y = 0
        self.sound = pygame.mixer.Sound("health.wav")

        self.create()

    def create(self):
        global num, points, fruits
        num = random.randint(0,2)
        fruits = ["Pumpkin.png","Watermelon.png","Tomato.png"]
        points = [1,3,9]
        self.y = -50
        self.x = random.randint(0,1400)

        self.image = pygame.transform.scale_by(pygame.image.load(fruits[num]), .15)
        self.zone = self.image.get_rect()
        self.points = points[num]
    
    def update(self,screen):
        screen.blit(self.image,(self.x, self.y))
        self.y +=self.points
        self.zone.y = self.y
        self.zone.x = self.x
        # pygame.draw.rect(screen,"red", self.zone)
        if self.y > 900:
            self.create()