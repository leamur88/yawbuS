import pygame
#Variables
s_width = 1250 #Screen Size
s_height = 750
x=50
y=690
b_width=100 #Background tiles
b_height=100
p_height=225 #progress bar
p_width=55
progress=200

win =pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Sandwich Time")
pygame.init()
run= True

#Background
win.fill((0,0,0))#Black Background
for col in range(0,s_width,b_width*2):#This is for the first set of rows and cols
    for row in range(0,s_height,b_height*2):
        pygame.draw.rect(win,(255,255,255),(col,row,b_width,b_height))
for col in range(b_width,s_width,b_width*2):#Second set of rows and cols
    for row in range(b_height,s_height,b_height*2):
        pygame.draw.rect(win,(255,255,255),(col,row,b_width,b_height))

pygame.draw.rect(win,(0,0,0),(0,0,250,s_height))#Black left Column
pygame.draw.rect(win,(0,0,255),(125-(p_width//2),s_height-p_height-5,p_width,p_height))#Progress Bar


pygame.display.update()

while  run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False


    pygame.display.update()
pygame.quit()
