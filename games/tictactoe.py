import numpy as np

class TicTacToe:
    
    def wincond(self, board, player):
        nboard = (board == player)

        # Horizontal (Check 5 consecutive columns)
        horizontal = (
            nboard[:, :-4] &
            nboard[:, 1:-3] &
            nboard[:, 2:-2] &
            nboard[:, 3:-1] &
            nboard[:, 4:]
        )

        # Vertical (Check 5 consecutive rows)
        vertical = (
            nboard[:-4, :] &
            nboard[1:-3, :] &
            nboard[2:-2, :] &
            nboard[3:-1, :] &
            nboard[4:, :]
        )

        # Diagonal 1 (Top-Left to Bottom-Right)
        diag1 = (
            nboard[:-4, :-4] &
            nboard[1:-3, 1:-3] &
            nboard[2:-2, 2:-2] &
            nboard[3:-1, 3:-1] &
            nboard[4:, 4:]
        )

        # Diagonal 2 (Bottom-Left to Top-Right)
        diag2 = (
            nboard[4:, :-4] &
            nboard[3:-1, 1:-3] &
            nboard[2:-2, 2:-2] &
            nboard[1:-3, 3:-1] &
            nboard[:-4, 4:]
        )

        return np.any(horizontal) or np.any(vertical) or np.any(diag1) or np.any(diag2)