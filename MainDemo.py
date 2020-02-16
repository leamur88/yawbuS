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
ham = pygame.image.load('leBurger.gif')
vel = 10
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

#Winning backgrounds
winner1 = pygame.image.load("lastScene1.png")
winner2 = pygame.image.load('lastScene2.png')
winner3 = pygame.image.load('lastScene3.png')
winState = winner1


win =pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Sandwich Time")
pygame.init()
run= True

class Ingredients:
    def __init__(self, image_id, type, select, cost):
        self.id = image_id
        self.type = type
        self.select = select
        self.cost = cost

#bread
GR = Ingredients("Golden Retriever.png", "bread", 'g', 100)
Huskie = Ingredients("Huskie.png", "bread", 'h', 100)
Dachshund = Ingredients("Dachshund.png", "bread", 'd', 100)

#meat
Heart = Ingredients("Heart.png", "meat", 'h', 5)
Brain = Ingredients("Brain.png", "meat", 'b', 2)
Liver = Ingredients("Liver.png", 'meat', 'l', 9)
Lung = Ingredients('Lung.png', 'meat', 'u', 4)

#veggie
FireHydrant = Ingredients("Fire Hydrant.png", 'veg', 'f', 5)
Limo = Ingredients("Limo.png", 'veg', 'l', 7)
Statue = Ingredients("Statue.png", 'veg', 's', 2)
Surfboard = Ingredients("Surfboard.png", 'veg', 'b', 3)

#sauce
Fire = Ingredients("Fire.png", "sauce", 'f', 2)
Mud = Ingredients("Mud.gif", "sauce", 'm', 3)
Slime = Ingredients("Slime.gif", 'sauce', 's', 8)

bread = [GR, Huskie, Dachshund]
meat = [Heart, Brain, Liver, Lung]
veggie = [FireHydrant, Limo, Statue, Surfboard]
sauce = [Fire, Mud, Slime]

class Hamburgers:
    def __init__(self, x,y,velo):
        self.x = x
        self.y =y
        self.orderSum = 0
        self.order = []
        self.velo=velo
        self.createOrder()

    def createOrder(self):
        self.order.append(random.choice(bread))
        self.order.append(random.choice(meat))
        self.order.append(random.choice(veggie))
        self.order.append(random.choice(sauce))
        self.order.append(self.order[0])

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
    textbox('Progress ($200)',125,s_height-p_height-10,green,black,22)
    textbox('$100',180,550,green,black,22)
    pygame.draw.rect(win,red,(100,550,p_width,5))
    textbox('$150',180,500,green,black,22)
    pygame.draw.rect(win,red,(100,500,p_width,5))
    textbox('$50',180,600,green,black,22)
    pygame.draw.rect(win,red,(100,600,p_width,5))
    pygame.draw.rect(win,green,(100,650-total_money,p_width,total_money))
    #Hamburgers
    win.blit(ham,(current_ham.x,current_ham.y))


    #Reciept
    textbox("Current Order",125,15,white,black,30)
    pygame.draw.rect(win,white,(0,30,250,5))

    pygame.draw.rect(win,light_gray,(20,45,210,300))


    textbox(current_ham.order[0].id[0: -4] + " [" + current_ham.order[0].select+']',125,60,black,light_gray,20)
    textbox(current_ham.order[1].id[0: -4] + " [" + current_ham.order[1].select+']',125,80,black,light_gray,20)
    textbox(current_ham.order[2].id[0: -4] + " [" + current_ham.order[2].select+']',125,100,black,light_gray,20)
    textbox(current_ham.order[3].id[0: -4] + " [" + current_ham.order[3].select+']',125,120,black,light_gray,20)







    #Sandwich progress
    counter=pygame.image.load("filled counter.jpg")
    pygame.draw.rect(win,gray,(250,250,200,300))
    win.blit(counter, (450, 250))
    textbox('Sandwich Progress',350,262,white,black,22)
    if ingredient_list[0]!=0:
        bread = pygame.image.load(ingredient_list[0].id)
        win.blit(bread, (300,270))
        win.blit(bread, (300,460))
    if ingredient_list[1]!=0:
        meat = pygame.image.load(ingredient_list[1].id)
        win.blit(meat, (300,400))
    if ingredient_list[2]!=0:
        veggie = pygame.image.load(ingredient_list[2].id)
        win.blit(veggie, (300,370))
    if ingredient_list[3]!=0:
        sauce = pygame.image.load(ingredient_list[3].id)
        win.blit(sauce, (300,300))
    #Movement
    if left:
        win.blit(walkLeft, (x,y))
    elif right:
        win.blit(walkRight, (x,y))
    else:
        win.blit(char, (x,y))


def textbox(text,x,y,fontcolor,backgroundcolor,fontsize): #Us this to make textboxes

    font = pygame.font.Font('freesansbold.ttf', fontsize)
    text = font.render(text, True, fontcolor, backgroundcolor)
    textRect = text.get_rect()
    textRect.center = (x,y)
    win.blit(text,textRect)


pygame.display.update()
n=0 #Hamburger counter
velocity=1  #Hamburger velocity
floatvelo=1
p=1 #final picture
while run:

    keys = pygame.key.get_pressed()

    if n==0:
        n=1
        current_ham = Hamburgers(1250,75,velocity)
    current_ham.x-=current_ham.velo
    if total_money < 200:
        if current_ham.x <=250:
            print("You have taken too long to complete the leBurger's order, better luck next time...")
            run=False
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
        ingredient_list[0] = GR
        ingredient_list[4] = GR
    elif keys[pygame.K_h] and x > 1045:
        ingredient_list[0] = Huskie
        ingredient_list[4] = Huskie
    elif keys[pygame.K_d] and x > 1045:
        ingredient_list[0] = Dachshund
        ingredient_list[4] = Dachshund

    #Meat
    elif keys[pygame.K_h] and x > 795 and x < 1045:
        ingredient_list[1] = Heart
    elif keys[pygame.K_b] and x > 795 and x < 1045:
        ingredient_list[1] = Brain
    elif keys[pygame.K_l] and x > 795 and x < 1045:
        ingredient_list[1] = Liver
    elif keys[pygame.K_u] and x > 795 and x < 1045:
        ingredient_list[1] = Lung

    #Veg
    elif keys[pygame.K_f] and x > 550 and x < 795:
        ingredient_list[2] = FireHydrant
    elif keys[pygame.K_l] and x > 550 and x < 795:
        ingredient_list[2] = Limo
    elif keys[pygame.K_s] and x > 550 and x < 795:
        ingredient_list[2] = Statue
    elif keys[pygame.K_b] and x > 550 and x < 795:
        ingredient_list[2] = Surfboard

    #Sauce
    elif keys[pygame.K_f] and x > 405 and x < 550:
        ingredient_list[3] = Fire
    elif keys[pygame.K_m] and x > 405 and x < 550:
        ingredient_list[3] = Mud
    elif keys[pygame.K_s] and x > 405 and x < 550:
        ingredient_list[3] = Slime

    if ingredient_list == current_ham.order:
        n=0
        floatvelo+=.25
        velocity=int(floatvelo//1)
        for ingred in ingredient_list:
            total_money+= ingred.cost
        ingredient_list=[0,0,0,0,0]
        pygame.time.delay(300)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    redrawGameWindow()
    if total_money>=200:
        if p==1:
            win.blit(winState, (0, 0))
            textbox("Press [E]",1150,325,white,black,22)
            textbox("to continue...",1150,350,white,black,22)
        elif p==2:
            winState = winner2
            win.blit(winState, (0, 0))
            textbox("Press [w]",1150,375,white,black,22)
            textbox("to continue...",1150,400,white,black,22)
        elif p==3:
            winState = winner3
            win.blit(winState, (0, 0))
            textbox("Press [q]",1150,375,white,black,22)
            textbox("to end...",1150,400,white,black,22)
        if keys[pygame.K_e]:
            p=2
            win.blit(winState, (0, 0))
            textbox("Press [w]",1150,375,white,black,22)
            textbox("to continue...",1150,400,white,black,22)
        elif keys[pygame.K_w]:
            p=3
        elif keys[pygame.K_q]:
            run=False
        # print("after winner1")
        # time.sleep(3)
        # win.blit(winner2, (0, 0))
        # time.sleep(3)
        # win.blit(winner3, (0, 0))
        # time.sleep(3)
        # run = False


    pygame.display.update()
pygame.quit()
