import numpy as np

class TicTacToe:
    
    def wincond(self,board,players):
        nboard = (board == players)

        #Horizontal
        horizontal = (
            nboard[:, :-4] &
            nboard[:, 1:-3] &
            nboard[:, 2:-2] &
            nboard[:, 3:-1] &
            nboard[:, 4:]
        )

        #Vertical
        vertical = (
            nboard[:-4, :] &
            nboard[1:-3, :] &
            nboard[2:-2, :] &
            nboard[3:-1, :] &
            nboard[4:, :]
        )

        #Diagonal1
        diag1 = (
            nboard[:-4, :-4] &
            nboard[1:-3, 1:-3] &
            nboard[2:-2, 2:-2] &
            nboard[3:-1, 3:-1] &
            nboard[4:, 4:]
        )

        #diag2
        diag2 = (
            nboard[:-4, 4:] &
            nboard[1:-3, 3:-1] &
            nboard[2:-2, 2:-2] &
            nboard[3:-1, 1:-3] &
            nboard[4:, :-4]
        )

        return np.any(horizontal) or np.any(vertical) or np.any(diag1) or np.any(diag2)