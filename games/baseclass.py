import numpy as np

class base:
    def __init__(self,p1,p2,n):
        self.p1=p1
        self.p2=p2
        self.turn=1
        self.board=np.zeros((n,n),dtype=int)
    def switchturn(self):
        self.turn=3-self.turn
    def record(winner, loser, game, player2=None):   
        fpath = Path("history.csv")
        date = time.strftime("%Y-%m-%d")
        if winner == "Tie":
            new_row = f"Tie,{loser},{player2},{date},{game}\n"
        else:
            new_row = f"{winner},{loser},_,{date},{game}\n"  # _ as empty placeholder
        with open(fpath, "a") as f:
            f.write(new_row)