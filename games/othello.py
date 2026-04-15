import pygame 
from sys import exit
import numpy as np
import sys
p1=sys.argv[1]
p2=sys.argv[2]
class Game:
    def __init__(self, p1, p2, sym1, sym2, n,c,state):
        self.p1 = p1
        self.p2 = p2
        self.sym1 = sym1
        self.sym2 = sym2
        self.n = np.zeros((n, n), dtype=int)
        self.state = state  
        self.c = c
        self.a=n

    def turn(self):
        current = self.state
        self.state = 1 - self.state
        return current
    

class othello:
#just the numbers
    def __init__(self,size):
        #update initial positions
        self.size=size
        self.board=np.zeros((size,size),dtype=int)
        self.board[size//2,size//2]=1
        self.board[size//2-1,size//2-1]=1
        self.board[size//2,size//2-1]=2
        self.board[size//2-1,size//2]=2
        
    def validmoves(self, player):
        options = np.zeros((self.size, self.size), dtype=int)

        for a in range(self.size):
            for b in range(self.size):
                if self.board[a, b] != 0:
                    continue
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x == 0 and y == 0:
                            continue
                        if self.inbounds(a+x, b+y):
                            if self.board[a+x, b+y] not in [0, player]:
                                u, i = self.checkfun(a+x, b+y, x, y, self.board, player)
                                if u != -1:
                                    options[a, b] = 1   
        return options

    def checkfun(self, p, q, x, y, tboard, play):
        while self.inbounds(p+x, q+y):
            p += x
            q += y
            if tboard[p, q] == 0:
                return (-1, -1)
            if tboard[p, q] == play:
                return (p, q)
        return (-1, -1)

    def inbounds(self,l,m)  :
        if l>=0 and l<self.size and m>=0 and m <self.size:
            return True
        else:
            return False
    def count(self):
        #count no of discs of each player
        p1,p2=0,0
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i,j]==1:
                    p1+=1
                if self.board[i,j]==2:
                    p2+=1
        return (p1,p2)
    
    def wincond(self,curr):
        #when the game ends
        
        choices=self.validmoves(curr+1)
        for i in range(self.size):
            for j in range(self.size):
                for p in range(self.size):
                    for q in range(self.size):
                        if choices[p,q]==1:
                            return False
        return True
    def makemove(self,a,b,player):
        if self.validmoves(player)[a,b]==1:
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    l=a
                    m=b
                    k=1
                    while self.inbounds(l+i,m+j) and k==1:
                        l+=i
                        m+=j
                        if self.board[l,m] not in [0,player]:
                            continue
                        if self.board[l,m] == player:
                            if i!=0:
                                g=(l-a)/i
                            if i==0:
                                g=0
                            if j!=0:
                                h=(m-b)/j
                            if j==0:
                                h=0
                            for p in range(max(int(g),int(h))):
                                    p+=1
                                    self.board[a+p*i,b+p*j]=player
                            break
                        if self.board[l,m]==0:
                            break
        self.board[a,b]=player
pygame.init()
screen=pygame.display.set_mode((1000,800))
pygame.display.set_caption("OTHELLO")
clock=pygame.time.Clock()
othboard=othello(8)
player=Game(p1,p2,1,2,8,4,0)
ticbg=pygame.image.load('../media/ticbg.png').convert()
ticbg=pygame.transform.scale(ticbg,(1000,800))

empty_surf=pygame.image.load('../media/emptyc4.png').convert()
empty_surf=pygame.transform.scale(empty_surf,(80,80))

x_surf=pygame.image.load('../media/disc1.png').convert()
x_surf=pygame.transform.scale(x_surf,(80,80))

o_surf=pygame.image.load('../media/disc2.png').convert()
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
        
        if event.type==pygame.MOUSEBUTTONDOWN and othboard.wincond(player.state)==False:
            mouse_pos=pygame.mouse.get_pos()
            for j in range(player.a):
                for i in range(player.a):
                    if x_rect[i][j].collidepoint(mouse_pos):
                        current=player.state
                        if 1 == 1:
                            if othboard.validmoves(current+1)[i,j]==1:
                                othboard.makemove(i,j,current+1)
                                player.turn()
                                for d in range(player.a):
                                    for s in range(player.a):
                                        if othboard.board[d,s]==1:
                                            surf[d][s] = x_surf
                                        if othboard.board[d,s]==2:
                                            surf[d][s] = o_surf 
    screen.blit(ticbg,(0,0))
    for d in range(player.a):
        for s in range(player.a):
            if othboard.board[d,s]==1:
                surf[d][s] = x_surf
            if othboard.board[d,s]==2:
                surf[d][s] = o_surf
    for i in range(player.a):
        for j in range(player.a):
            screen.blit(surf[i][j],x_rect[i][j])
    l1,l2=othboard.count()       
    fonts=pygame.font.Font(None,100)
    texts=fonts.render(f"player1 : {l1} player2 : {l2}",False,(255,255,255))
    texts_rect=texts.get_rect(center=(500,100))
    screen.blit(texts,texts_rect)

    if othboard.wincond(player.state):
        pl1,pl2=othboard.count()
        if pl1>pl2: 
            font=pygame.font.Font(None,100)
            text=font.render(f"{p1} wins", False,(255,255,255))
            text_rect=text.get_rect(center=(400,400))
            screen.blit(text,text_rect)
        if pl1<pl2:
            font=pygame.font.Font(None,100)
            text=font.render(f"{p2} wins", False,(255,255,255))
            text_rect=text.get_rect(center=(400,400))
            screen.blit(text,text_rect)
        if pl1==pl2:
            font=pygame.font.Font(None,100)
            text=font.render("TIE", False,(255,255,255))
            text_rect=text.get_rect(center=(400,400))
            screen.blit(text,text_rect)
    pygame.display.update()
    clock.tick(60)


    
