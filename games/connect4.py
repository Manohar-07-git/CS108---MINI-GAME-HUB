import numpy as np
import pygame 
from sys import exit
import sys
print("running")
p1=sys.argv[1]
p2=sys.argv[2]

class Game:
    def __init__(self, p1, p2, sym1, sym2, n,c):
        self.p1 = p1
        self.p2 = p2
        self.sym1 = sym1
        self.sym2 = sym2
        self.n = np.zeros((n, n), dtype=int)
        self.state = 0  
        self.c = c
        self.a=n

    def turn(self):
        current = self.state
        self.state = 1 - self.state
        return current

    def wincond(self):
        #horizontal
        for i in range(self.a):
            for j in range((self.a-self.c)+1):
                countx=0
                counto=0
                for k in range(self.c):
                    if self.n[i][j+k]==1:
                        countx+=1
                    if self.n[i][j+k]==2:
                        counto+=1
                if countx==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i][j+self.c-1].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p1} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True
                if counto==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i][j+self.c-1].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p2} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True

        #vertical
        for j in range(self.a):
            for i in range((self.a-self.c)+1):
                countx=0
                counto=0
                for k in range(self.c):
                    if self.n[i+k][j]==1:
                        countx+=1
                    if self.n[i+k][j]==2:
                        counto+=1
                if countx==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i+self.c-1][j].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p1} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True
                if counto==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i+self.c-1][j].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p2} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True

        #diagonal 
        for i in range(self.a - self.c + 1):
            for j in range(self.a - self.c + 1):
                countx=0
                counto=0
                for k in range(self.c):
                    if self.n[i+k][j+k]==1:
                        countx+=1
                    if self.n[i+k][j+k]==2:
                        counto+=1

                if countx==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i+self.c-1][j+self.c-1].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p1} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True

                if counto==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i+self.c-1][j+self.c-1].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p2} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True

        #diagonal 
        for i in range(self.a - self.c + 1):
            for j in range(self.c - 1, self.a):
                countx=0
                counto=0
                for k in range(self.c):
                    if self.n[i+k][j-k]==1:
                        countx+=1
                    if self.n[i+k][j-k]==2:
                        counto+=1

                if countx==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i+self.c-1][j-(self.c-1)].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p1} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True

                if counto==self.c:
                    pygame.draw.line(screen,(255,255,255),x_rect[i][j].center,x_rect[i+self.c-1][j-(self.c-1)].center,5)
                    font=pygame.font.Font(None,100)
                    self.text=font.render(f"{self.p2} WON", False,(0,255,255))
                    self.text_rect=self.text.get_rect(center=(400,400))
                    return True

        #tie
        for i in range(self.a):
            for j in range(self.a):
                if self.n[i][j]==0:
                    return False

        print("tie") 
        font=pygame.font.Font(None,100)
        self.text=font.render("TIE", False,(0,255,255))
        self.text_rect=self.text.get_rect(center=(400,400))
        return True


pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("CONNECT 4")
clock=pygame.time.Clock()

player=Game(p1,p2,0,1,7,4)

ticbg=pygame.image.load('../media/ticbg.png').convert()
ticbg=pygame.transform.scale(ticbg,(1000,800))

empty_surf=pygame.image.load('../media/empty.png').convert()
empty_surf=pygame.transform.scale(empty_surf,(80,80))

x_surf=pygame.image.load('../media/x.png').convert()
x_surf=pygame.transform.scale(x_surf,(80,80))

o_surf=pygame.image.load('../media/o.png').convert()
o_surf=pygame.transform.scale(o_surf,(80,80))

x_rect=[]
surf=[]

for j in range(player.a):
    xv_rect=[]
    surfv=[]
    for i in range(player.a):
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

        if event.type==pygame.MOUSEBUTTONDOWN and player.wincond()==0:
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

    if player.wincond():
        screen.blit(player.text,player.text_rect)
    pygame.display.update()
    clock.tick(60)
