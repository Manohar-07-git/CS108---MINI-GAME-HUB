import numpy as np 
class othello:

    def __init__(self,size):
        
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
    def count(self):
        a=np.sum(self.board==1)
        b=np.sum(self.board==2)
        return (a,b)

    def wincond(self,player):
        self.player=player
        if np.all(self.validmoves(player)==0):
            return True
        return False