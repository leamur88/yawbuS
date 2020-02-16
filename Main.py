import pygame
import time
#Variables
s_width = 1250 #Screen Size
s_height = 650
x=750
y=550
b_width=100 #Background tiles
b_height=100
p_height=200 #progress bar
p_width=55
progress=200

#moving
walkRight = pygame.image.load('guy_right.png')
walkLeft = pygame.image.load('guy_left.png')
char = pygame.image.load('guy_up.png')
vel = 5
left = False
right = False

#Colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

total_money = 0

win =pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Sandwich Time")
pygame.init()
run= True

class Ingredients:
    def __init__(self, image_id, type, select):
        self.id = id
        self.type = type


GR = Ingredients("Golden_Retriever.png", "bread", 'g')
Huskie = Ingredients("Huskie.png", "bread", 'h')
Dachshund = Ingredients("Dachshund.png", "bread", 'd')

Heart = Ingredients("heart.png", "meat", 'h')
Brain = Ingredients("brain.png", "meat", 'b')
Liver = Ingredients("liver.png", 'meat', 'l')
Lung = Ingredients('lung.png', 'meat', 'p')

FireHydrant = Ingredients("firehydrant.png", 'veg', 'f')
Limo = Ingredients("limo.png", 'veg', 'a')
Statue = Ingredients("statue.png", 'veg', 's')
Surfboard = Ingredients("surfboard.png", 'veg', 'b')

Fire = Ingredients("fire,png", "sauce", 'f')
Mud = Ingredients("mud.gif", "sauce", 'm')
Slime = Ingredients("Slime.gif", 'sauce', 's')

menu = [Heart, Brain, Liver, Pancreas, FireHydrant, Limo, Statue, Surfboard, Fire, Mud, Slime]
bread = [GR, Huskie, Dachshund]
class Hamburgers:
    def __init__(self, x, order):
        print("")




def redrawGameWindow():
    #Background
    win.fill((0,0,0))#Black Background
    for col in range(0,s_width,b_width*2):#This is for the first set of rows and cols
        for row in range(0,s_height,b_height*2):
            pygame.draw.rect(win,(255,255,255),(col,row,b_width,b_height))
    for col in range(b_width,s_width,b_width*2):#Second set of rows and cols
        for row in range(b_height,s_height,b_height*2):
            pygame.draw.rect(win,(255,255,255),(col,row,b_width,b_height))
    pygame.draw.rect(win,(0,0,0),(0,0,250,s_height))#Black left Column
    pygame.draw.rect(win,blue,(125-(p_width//2),s_height-p_height-5,p_width,p_height))#Progress Bar
    textbox('Progress',125,s_height-p_height-10,green,black)

    counter=pygame.image.load("marblecounter.jpg")
    win.blit(counter, (450, 250))
    if left:
        win.blit(walkLeft, (x,y))
    elif right:
        win.blit(walkRight, (x,y))
    else:
        win.blit(char, (x,y))

#Progress Bar
def textbox(text,x,y,fontcolor,backgroundcolor): #Us this to make textboxes

    font = pygame.font.Font('freesansbold.ttf', 22)
    text = font.render(text, True, fontcolor, backgroundcolor)
    textRect = text.get_rect()
    textRect.center = (x,y)
    win.blit(text,textRect)


pygame.display.update()

while  run:

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 250+vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < s_width - 90 - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    redrawGameWindow()
    pygame.display.update()
pygame.quit()
