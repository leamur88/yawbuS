import pygame
import time
import random
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
red=(255,0,0)
dark_gray=(47,79,79)
light_gray=(211,211,211)


win =pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Sandwich Time")
pygame.init()
run= True

class Ingredients:
    def __init__(self, image_id, type, select, cost):
        self.id = id
        self.type = type
        self.select = select
        self.cost = cost


GR = Ingredients("Golden_Retriever.png", "bread", 'g', 10)
Huskie = Ingredients("Huskie.png", "bread", 'h', 10)
Dachshund = Ingredients("Dachshund.png", "bread", 'd', 10)

Heart = Ingredients("heart.png", "meat", 'h', 10)
Brain = Ingredients("brain.png", "meat", 'b', 10)
Liver = Ingredients("liver.png", 'meat', 'l', 10)
Lung = Ingredients('lung.png', 'meat', 'p', 10)

FireHydrant = Ingredients("firehydrant.png", 'veg', 'f', 10)
Limo = Ingredients("limo.png", 'veg', 'a', 10)
Statue = Ingredients("statue.png", 'veg', 's', 10)
Surfboard = Ingredients("surfboard.png", 'veg', 'b', 10)

Fire = Ingredients("fire,png", "sauce", 'f', 10)
Mud = Ingredients("mud.gif", "sauce", 'm', 10)
Slime = Ingredients("Slime.gif", 'sauce', 's', 10)

menu = [Heart, Brain, Liver, Lung, FireHydrant, Limo, Statue, Surfboard, Fire, Mud, Slime]
bread = [GR, Huskie, Dachshund]
class Hamburgers:
    def __init__(self, x):
        self.x = x
        self.order = []
        createOrder()
    def createOrder():
        self.order.append(bread.randomChoice())
        for i in range(3):
            self.order.append(menu.randomChoice())






def redrawGameWindow():
    #Background
    win.fill(light_gray)#Black Background
    for col in range(0,s_width,b_width*2):#This is for the first set of rows and cols
        for row in range(0,s_height,b_height*2):
            pygame.draw.rect(win,dark_gray,(col,row,b_width,b_height))
    for col in range(b_width,s_width,b_width*2):#Second set of rows and cols
        for row in range(b_height,s_height,b_height*2):
            pygame.draw.rect(win,dark_gray,(col,row,b_width,b_height))
    pygame.draw.rect(win,(0,0,0),(0,0,250,s_height))#Black left Column
    pygame.draw.rect(win,blue,(125-(p_width//2),s_height-p_height-5,p_width,p_height))#Progress Bar
<<<<<<< HEAD
    textbox('Progress (200$)',125,s_height-p_height-10,green,black)
    textbox('$100',180,550,green,black)
    pygame.draw.rect(win,red,(100,550,p_width,5))
    textbox('$150',180,500,green,black)
    pygame.draw.rect(win,red,(100,500,p_width,5))
    textbox('$50',180,600,green,black)
    pygame.draw.rect(win,red,(100,600,p_width,5))
    pygame.draw.rect(win,green,(100,650-total_money,p_width,total_money))
=======
    textbox('Progress',125,s_height-p_height-10,green,black)
>>>>>>> 25a9a89eca198fff7e8148ce306ed34478b40f38

    counter=pygame.image.load("filledcounter.jpg")
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

    if total_money >=200:
        win.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    redrawGameWindow()
    pygame.display.update()
pygame.quit()
