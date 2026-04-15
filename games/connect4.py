import numpy as np
import pygame 
from sys import exit
import sys
p1=sys.argv[1]
p2=sys.argv[2]
from game import Game




pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("CONNECT 4")
clock=pygame.time.Clock()

player=Game(p1,p2,7,4,0)

ticbg=pygame.image.load('./media/ticbg.png').convert()
ticbg=pygame.transform.scale(ticbg,(1000,800))

empty_surf=pygame.image.load('./media/emptyc4.png').convert()
empty_surf=pygame.transform.scale(empty_surf,(80,80))

x_surf=pygame.image.load('./media/disc1.png').convert()
x_surf=pygame.transform.scale(x_surf,(80,80))

o_surf=pygame.image.load('./media/disc2.png').convert()
o_surf=pygame.transform.scale(o_surf,(80,80))

x_rect=[]
surf=[]

for j in range(player.a):
    xv_rect=[]
    surfv=[]
    for i in range(player.a):
        rect_x=x_surf.get_rect(topleft=(220+(player.a-i-1)*80,120+(player.a-j-1)*80))
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
            for j in range(player.a):
                for i in range(player.a):
                    if x_rect[i][j].collidepoint(mouse_pos):
                        for h in range(i+1):
                            if surf[h][j] is empty_surf:
                                current = player.turn()
                                if current==0:    
                                    surf[h][j]=x_surf
                                    player.n[h][j]=1
                                    break
                                else:
                                    surf[h][j]=o_surf
                                    player.n[h][j]=2
                                    break

    screen.blit(ticbg,(0,0))

    for i in range(player.a):
        for j in range(player.a):
            screen.blit(surf[i][j],x_rect[i][j])

    if player.wincond(screen,x_rect):
        screen.blit(player.text,player.text_rect)
    pygame.display.update()
    clock.tick(60)