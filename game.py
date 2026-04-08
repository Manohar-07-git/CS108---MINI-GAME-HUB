from sys import exit
import numpy as np
import pygame as pg 
#user0
#user1
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
test_surface=pg.image.load('media/background.png')
test_surface=pg.transform.scale(test_surface,(1000,800))
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
    screen.blit(test_surface,(0,0))
    pg.display.update() 
    clock.tick(60)








