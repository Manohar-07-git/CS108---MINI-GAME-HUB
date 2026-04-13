from sys import exit
import numpy as np
import pygame as pg 
import subprocess
import sys
player1=sys.argv[1]
player2=sys.argv[2]
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

pg.init()
screen=pg.display.set_mode((1000,800))
pg.display.set_caption("GAME HUB!!!")
clock=pg.time.Clock()
bg_surf=pg.image.load('../media/background.png').convert()
bg_surf=pg.transform.scale(bg_surf,(1000,800))
tic_surf=pg.image.load('../media/tic tac toe.png').convert()
tic_surf=pg.transform.scale(tic_surf,(200,200))
tic_rect=tic_surf.get_rect(topleft=(125,400))
oth_surf=pg.image.load('../media/othello.png')
oth_surf=pg.transform.scale(oth_surf,(200,200))
oth_rect=oth_surf.get_rect(topleft=(375,400))
c4_surf=pg.image.load('../media/connect 4.png').convert()
c4_surf=pg.transform.scale(c4_surf,(200,200))
c4_rect=c4_surf.get_rect(topleft=(625,400))
font=pg.font.Font(None, 100)
text=font.render("GAME HUB", False,(0,255,255))
text_rect=text.get_rect(center=(500,300))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.MOUSEBUTTONDOWN:
            mouse_pos=pg.mouse.get_pos()
            if tic_rect.collidepoint(mouse_pos): 
                print("running")
                subprocess.run(["py","-3.11","./tictactoe.py", player1,player2])
                pg.quit()
                exit()
            if oth_rect.collidepoint(mouse_pos): 
                subprocess.run(["py","-3.11","othello.py",player1,player2])
                pg.quit()
                exit()
            if c4_rect.collidepoint(mouse_pos): 
                subprocess.run(["py","-3.11","./connect4.py",player1,player2])
                pg.quit()
                exit()

    screen.blit(bg_surf,(0,0))
    screen.blit(tic_surf,tic_rect)
    screen.blit(oth_surf,oth_rect)
    screen.blit(c4_surf,c4_rect)
    screen.blit(text,text_rect)
    pg.display.update() 
    clock.tick(60)








