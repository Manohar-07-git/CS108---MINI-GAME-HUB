from sys import exit
import numpy as np
import pygame as pg 
import subprocess
#player1=sys.argv[1]
#player2=sys.argv[2]
class player:
    def pint(self,name,symbol):
        self.name=name 
        self.symbol=symbol
    def board(self,size):
        self.size=size
        self.board=np.empty((size,size),dtype=np.uint8)
    def switch(self):
        if self.symbol==1:
            self.symbol=2
        else:
            self.symbol=1   

pg.init()
screen=pg.display.set_mode((1000,800))
pg.display.set_caption("GAME HUB!!!")
clock=pg.time.Clock()
bg_surf=pg.image.load('media/background.png').convert()
bg_surf=pg.transform.scale(bg_surf,(1000,800))
tic_surf=pg.image.load('media/tic tac toe.png').convert()
tic_surf=pg.transform.scale(tic_surf,(200,200))
tic_rect=tic_surf.get_rect(topleft=(125,400))
oth_surf=pg.image.load('media/othello.png')
oth_surf=pg.transform.scale(oth_surf,(200,200))
oth_rect=oth_surf.get_rect(topleft=(375,400))
c4_surf=pg.image.load('media/connect 4.png').convert()
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
                #subprocess.run(["py -3.11","tictactoe.py",player1,player2])
                pg.quit()
                exit()
            if oth_rect.collidepoint(mouse_pos): 
                #subprocess.run(["py -3.11","othello.py",player1,player2])
                pg.quit()
                exit()
            if c4_rect.collidepoint(mouse_pos): 
                #subprocess.run(["py -3.11","connect4.py",player1,player2])
                pg.quit()
                exit()

    screen.blit(bg_surf,(0,0))
    screen.blit(tic_surf,tic_rect)
    screen.blit(oth_surf,oth_rect)
    screen.blit(c4_surf,c4_rect)
    screen.blit(text,text_rect)
    pg.display.update() 
    clock.tick(60)








