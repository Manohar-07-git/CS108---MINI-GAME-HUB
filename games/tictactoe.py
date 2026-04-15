import numpy as np
import pygame 
from sys import exit
import sys
print("running")
p1=sys.argv[1]
p2=sys.argv[2]

from game import Game

pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("TIC TAC TOE")
clock=pygame.time.Clock()

player=Game(p1,p2,10,5,0)

ticbg=pygame.image.load('media/ticbg.png').convert()
ticbg=pygame.transform.scale(ticbg,(1000,800))

empty_surf=pygame.image.load('./media/empty.png').convert()
empty_surf=pygame.transform.scale(empty_surf,(80,80))

x_surf=pygame.image.load('./media/x.png').convert()
x_surf=pygame.transform.scale(x_surf,(80,80))

o_surf=pygame.image.load('./media/o.png').convert()
o_surf=pygame.transform.scale(o_surf,(80,80))

x_rect=[]
surf=[]

for j in range(10):
    xv_rect=[]
    surfv=[]
    for i in range(10):
        rect_x=x_surf.get_rect(topleft=(j*80,i*80))
        xv_rect.append(rect_x)
        surfv.append(empty_surf)
    x_rect.append(xv_rect)
    surf.append(surfv)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.MOUSEBUTTONDOWN and player.wincond(screen,x_rect)==0:
            mouse_pos=pygame.mouse.get_pos()
            for j in range(10):
                for i in range(10):
                    if x_rect[i][j].collidepoint(mouse_pos):
                        if surf[i][j] is empty_surf:
                            current = player.turn()

                            if current==0:    
                                surf[i][j]=x_surf
                                player.n[i][j]=1
                            else:
                                surf[i][j]=o_surf
                                player.n[i][j]=2

    screen.blit(ticbg,(0,0))

    for i in range(10):
        for j in range(10):
            screen.blit(surf[i][j],x_rect[i][j])

    if player.wincond(screen,x_rect):
        screen.blit(player.text,player.text_rect)
    pygame.display.update()
    clock.tick(60)