import pygame
import random
import pdb

pygame.init()

myfont = pygame.font.SysFont("style", 20)
blueCol = (0, 0, 255)
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Robo Game")

#pdb.set_trace()
xval = random.randint(100,400)
xleftover = xval % 50
x= xval - xleftover

yval = random.randint(100,400)
yleftover = yval % 50
y= yval - yleftover

width = 50
height = 50
vel = 50
clock = pygame.time.Clock()
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    win.fill((0, 0, 0))

    textobj = myfont.render("To win you should move UP by {0} steps and Left by {1} steps".format(str(y/50 -1),str(x/50 -1)), 10, blueCol)
    win.blit(textobj, (50, 10))
    if(x==50 and y==50):
        textobj = myfont.render("Congratulations You WIN !!!".format(x, y), 10, blueCol)
        win.blit(textobj, (50, 30))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    clock.tick(200)
pygame.quit()
