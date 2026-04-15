from sys import exit
import numpy as np
import pygame 
import subprocess
import sys
player1=sys.argv[1]
player2=sys.argv[2]

class Game:

    def __init__(self,p1,p2, n,c,state):
        self.p1 =p1
        self.p2=p2
        self.n = np.zeros((n, n), dtype=int)
        self.state = state
        self.c = c
        self.a=n

               

    def turn(self):
        current = self.state
        self.state = 1 - self.state
        return current

    def wincond(self,screen,x_rect):
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


if __name__ == "__main__":
    pygame.init()
    screen=pygame.display.set_mode((1000,800))
    pygame.display.set_caption("GAME HUB!!!")
    clock=pygame.time.Clock()
    bg_surf=pygame.image.load('media/background.png').convert()
    bg_surf=pygame.transform.scale(bg_surf,(1000,800))
    tic_surf=pygame.image.load('media/tic tac toe.png').convert()
    tic_surf=pygame.transform.scale(tic_surf,(200,200))
    tic_rect=tic_surf.get_rect(topleft=(125,400))
    oth_surf=pygame.image.load('media/othello.png')
    oth_surf=pygame.transform.scale(oth_surf,(200,200))
    oth_rect=oth_surf.get_rect(topleft=(375,400))
    c4_surf=pygame.image.load('media/connect 4.png').convert()
    c4_surf=pygame.transform.scale(c4_surf,(200,200))
    c4_rect=c4_surf.get_rect(topleft=(625,400))
    font=pygame.font.Font(None, 100)
    text=font.render("GAME HUB", False,(0,255,255))
    text_rect=text.get_rect(center=(500,300))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if tic_rect.collidepoint(mouse_pos): 
                    print("running")
                    pygame.quit()
                    
                    subprocess.run(["python3","./tictactoe.py", player1,player2])
                    exit()
                if oth_rect.collidepoint(mouse_pos): 
                    pygame.quit()
                    
                    subprocess.run(["python3","othello.py",player1,player2])
                    exit()
                if c4_rect.collidepoint(mouse_pos): 
                    pygame.quit()

                    subprocess.run(["python3","./connect4.py",player1,player2])
                    exit()                    

        screen.blit(bg_surf,(0,0))
        screen.blit(tic_surf,tic_rect)
        screen.blit(oth_surf,oth_rect)
        screen.blit(c4_surf,c4_rect)
        screen.blit(text,text_rect)
        pygame.display.update() 
        clock.tick(60)