import numpy as np

class c4:
    
    def wincond(self,board,player):
        nboard = (board == player)

        # Horizontal 
        horizontal = (
            nboard[:, :-3] &
            nboard[:, 1:-2] &
            nboard[:, 2:-1] &
            nboard[:, 3:]
        )

        # Vertical
        vertical = (
            nboard[:-3, :] &
            nboard[1:-2, :] &
            nboard[2:-1, :] &
            nboard[3:, :]
        )

        # Diag1
        diag1 = (
            nboard[:-3, :-3] &
            nboard[1:-2, 1:-2] &
            nboard[2:-1, 2:-1] &
            nboard[3:, 3:]
        )

        # diag2
        diag2 = (
            nboard[:-3, 3:] &
            nboard[1:-2, 2:-1] &
            nboard[2:-1, 1:-2] &
            nboard[3:, :-3]
        )

        return np.any(horizontal) or np.any(vertical) or np.any(diag1) or np.any(diag2)