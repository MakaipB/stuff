import pygame
pygame.init()
from fruit import Fruit
from kirb import Kirb

clock = pygame.time.Clock()
KIRBY = Kirb()
# kirby = pygame.transform.scale(pygame.image.load("Kirby_Standing.png"), (100,90))
# k_hitbox = kirby.get_rect()
base = pygame.image.load("Ground.png")
base = pygame.transform.scale(base,(900,200))
# kirby_fly = pygame.transform.scale(pygame.image.load("kirbyflight.png"), (100,90))
# kirby_inhale_1 = pygame.transform.scale(pygame.image.load("kirbyinhale1.png"), (100,90))
# kirby_inhale_2 = pygame.transform.scale(pygame.image.load("kirbyinhale2.png"), (100,90))
pumpkin = pygame.image.load("Pumpkin.png")
tomato = pygame.image.load("Tomato.png")
watermelon = pygame.image.load("Watermelon.png")
waddle_dee = pygame.image.load("waddle_dee.png")
font = pygame.font.SysFont("timesnewroman", 45)
pygame.mixer.music.load("Gourmet Race.mp3")
width = 1440
height = 900
screen = pygame.display.set_mode((width,height))
running = True
ground = (width//4-100,height//2, width//4+800,height//2)
left_wall = (width//4-99,height//2,width//4-99,height//2+300)
right_wall = (width//4+801,height//2,width//4+801,height//2+300)
# p_x = 400
# p_y = 50
# p_xspeed = 0
# p_yspeed = 0
# grounded = False
fruits = [Fruit() for _ in range(5)]
score = 0
# kirby_frame = kirby
# facing_left = False


# def moving():
#     global p_xspeed, p_x, p_y, p_yspeed,k_hitbox, grounded, score, facing_left
#     keys_pressed = pygame.key.get_pressed()
#     if keys_pressed[pygame.K_a]:
#         facing_left = True
#         p_xspeed = max(p_xspeed - 1, -8)
#     elif keys_pressed[pygame.K_d]:
#         facing_left = False
#         p_xspeed = min(p_xspeed + 1, +8)
#     else:
#         p_xspeed *=.8
#     p_x+=p_xspeed

#     if keys_pressed[pygame.K_w] and grounded:
#         p_yspeed = -30
#     elif grounded:
#         p_yspeed = 0
#     else:
#         p_yspeed = min(p_yspeed+2, 20)
#     p_y+=p_yspeed
#     k_hitbox.x = p_x
#     k_hitbox.y = p_y

#     if k_hitbox.clipline(ground):
#         grounded = True
#         while k_hitbox.bottom > ground[1] +.1:
#             p_y-=1
#             k_hitbox.y = p_y
#     else:
#         grounded = False
    
#     if k_hitbox.y>900:
#         p_y = 0
#         p_x = 700
#         score-= 20


# def animation():
#     global grounded, kirby_frame, kirby_fly, kirby, p_yspeed
#     if grounded is False and p_yspeed != 0:
#         kirby_frame = kirby_fly
#     if grounded:
#         kirby_frame = kirby
    
        



pygame.mixer.music.play(-1)
while running:
    clock.tick(60)
    screen.fill((224,255,255))
    screen.blit(base, (width//4-100,height//2))
    KIRBY.update(screen)
    # screen.blit(pygame.transform.flip(kirby_frame, facing_left, False), (p_x,p_y))
    scoreTXT = font.render(f"{KIRBY.score}", True, "black")

    
    for event in pygame.event.get():
        if score >= 200:
            running = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    # moving()
    # animation()
    for fruit in fruits:
        fruit.update(screen)
        if KIRBY.hitbox.colliderect(fruit.zone):
            KIRBY.score+= fruit.points
            fruit.sound.play()
            fruit.create()
    
    screen.blit(scoreTXT, (0,0,0,0))





    pygame.display.update()