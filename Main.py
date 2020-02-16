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
total_money=0

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
gray=(128,128,128)

#list of ingredients
ingredient_list = [0, 0, 0, 0, 0]

total_money = 0

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

ingredients=["Golden_Retriever.png","heart.png","brain.png","limo.png","Golden_Retriever.png"]


GR = Ingredients("Golden_Retriever.png", "bread", 'g', 10)
Huskie = Ingredients("Huskie.png", "bread", 'h', 10)
Dachshund = Ingredients("Dachshund.png", "bread", 'd', 10)

Heart = Ingredients("heart.png", "meat", 'h', 10)
Brain = Ingredients("brain.png", "meat", 'b', 10)
Liver = Ingredients("liver.png", 'meat', 'l', 10)
Lung = Ingredients('lung.png', 'meat', 'u', 10)

FireHydrant = Ingredients("firehydrant.png", 'veg', 'f', 10)
Limo = Ingredients("limo.png", 'veg', 'l', 10)
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
        self.orderSum = 0
        self.order = []
        createOrder()

    def createOrder():
        self.order.append(bread.randomChoice())
        for i in range(3):
            self.order.append(menu.randomChoice())
            self.orderSum = self.orderSum + self.order[i].cost

def redrawGameWindow():
    #Background
    win.fill(light_gray)
    for col in range(0,s_width,b_width*2):#This is for the first set of rows and cols
        for row in range(0,s_height,b_height*2):
            pygame.draw.rect(win,dark_gray,(col,row,b_width,b_height))
    for col in range(b_width,s_width,b_width*2):#Second set of rows and cols
        for row in range(b_height,s_height,b_height*2):
            pygame.draw.rect(win,dark_gray,(col,row,b_width,b_height))
    pygame.draw.rect(win,(0,0,0),(0,0,250,s_height))#Black left Column
    pygame.draw.rect(win,blue,(125-(p_width//2),s_height-p_height-5,p_width,p_height))#Progress Bar
    #Progress Bar
    textbox('Progress (200$)',125,s_height-p_height-10,green,black,22)
    textbox('$100',180,550,green,black,22)
    pygame.draw.rect(win,red,(100,550,p_width,5))
    textbox('$150',180,500,green,black,22)
    pygame.draw.rect(win,red,(100,500,p_width,5))
    textbox('$50',180,600,green,black,22)
    pygame.draw.rect(win,red,(100,600,p_width,5))
    pygame.draw.rect(win,green,(100,650-total_money,p_width,total_money))
    #Sandwich progress
    counter=pygame.image.load("filledcounter.jpg")
    pygame.draw.rect(win,gray,(250,250,200,300))
    win.blit(counter, (450, 250))
    textbox('Sandwich Progress',350,262,white,black,22)
    if ingredients[0]!=0:
        bread = pygame.image.load(ingredients[0])
        win.blit(bread, (300,20))
        win.blit(bread, (300,400))
    if ingredients[1]!=0:
        meat = pygame.image.load(ingredients[1])
        win.blit(meat, (300,110))
    if ingredients[2]!=0:
        veggie = pygame.image.load(ingredients[2])
        win.blit(veggie, (300,200))
    if ingredients[3]!=0:
        sauce = pygame.image.load(ingredients[3])
        win.blit(sauce, (300,300))
    if left:
        win.blit(walkLeft, (x,y))
    elif right:
        win.blit(walkRight, (x,y))
    else:
        win.blit(char, (x,y))

#Progress Bar
def textbox(text,x,y,fontcolor,backgroundcolor,fontsize): #Us this to make textboxes

    font = pygame.font.Font('freesansbold.ttf', fontsize)
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

    #Bread
    if keys[pygame.K_g] and x > 1045:
        ingredient_list[0] = "Golden_Retriever.png"
        ingredient_list[4] = "Golden_Retriever.png"
    elif keys[pygame.K_h] and x > 1045:
        ingredient_list[0] = "Huskie.png"
        ingredient_list[4] = "Huskie.png"
    elif keys[pygame.K_d] and x > 1045:
        ingredient_list[0] = "Dachshund.png"
        ingredient_list[4] = "Dachshund.png"

    #Meat
    elif keys[pygame.K_h] and x > 795 and x < 1045:
        ingredient_list[1] = "heart.png"
    elif keys[pygame.K_b] and x > 795 and x < 1045:
        ingredient_list[1] = "brain.png"
    elif keys[pygame.K_l] and x > 795 and x < 1045:
        ingredient_list[1] = "liver.png"
    elif keys[pygame.K_u] and x > 795 and x < 1045:
        ingredient_list[1] = "lung.png"

    #Veg
    elif keys[pygame.K_f] and x > 550 and x < 795:
        ingredient_list[2] = "firehydrant.png"
    elif keys[pygame.K_l] and x > 550 and x < 795:
        ingredient_list[2] = "limo.png"
    elif keys[pygame.K_s] and x > 550 and x < 795:
        ingredient_list[2] = "statue.png"
    elif keys[pygame.K_b] and x > 550 and x < 795:
        ingredient_list[2] = "surfboard.png"

    #Sauce
    elif keys[pygame.K_f] and x > 405 and x < 550:
        ingredient_list[3] = "fire.png"
    elif keys[pygame.K_m] and x > 405 and x < 550:
        ingredient_list[3] = "mud.gif"
    elif keys[pygame.K_s] and x > 405 and x < 550:
        ingredient_list[3] = "Slime.gif"

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
#1045
#795
#550
#405
    redrawGameWindow()
    pygame.display.update()
pygame.quit()
