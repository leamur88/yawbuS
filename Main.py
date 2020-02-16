import math
import pygame
s_width = 1250
s_height = 750
win =pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Sandwich Time")

run= True

x=50
y=690
b_width=100
b_height=100
win.fill((0,0,0))
#Background
for col in range(0,s_width,b_width*2):#This is for the first set of rows and cols
    for row in range(0,s_height,b_height*2):
        pygame.draw.rect(win,(255,255,255),(col,row,b_width,b_height))
for col in range(b_width,s_width,b_width*2):#Second set of rows and cols
    for row in range(b_height,s_height,b_height*2):
        pygame.draw.rect(win,(255,255,255),(col,row,b_width,b_height))

print("done")
pygame.display.update()



#Keep (makes the game not break)
while  run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
pygame.quit()
