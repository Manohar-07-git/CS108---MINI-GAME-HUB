from sys import exit
import numpy as np
import pygame
import subprocess
import sys

player1 = sys.argv[1]
player2 = sys.argv[2]


class Game:

    def __init__(self, p1, p2, n, c, state):
        self.p1 = p1
        self.p2 = p2
        self.n = np.zeros((n, n), dtype=int)
        self.state = state
        self.c = c
        self.a = n
        self.winner = None
        self.Looser = None
        self.game_over = False

    def turn(self):
        current = self.state
        self.state = 1 - self.state
        return current

    def save_result(self):
        subprocess.run([
            "bash",
            "leaderboard.sh",
            self.winner,
            self.Looser
        ])

    def wincond(self, screen, x_rect):

        # horizontal
        for i in range(self.a):
            for j in range(self.a - self.c + 1):
                countx = 0
                counto = 0

                for k in range(self.c):
                    if self.n[i][j + k] == 1:
                        countx += 1
                    if self.n[i][j + k] == 2:
                        counto += 1

                if countx == self.c:
                    self.winner = self.p1
                    self.Looser = self.p2
                    self.game_over = True
                    self.save_result()
                    return True

                if counto == self.c:
                    self.winner = self.p2
                    self.Looser = self.p1
                    self.game_over = True
                    self.save_result()
                    return True

        # vertical
        for j in range(self.a):
            for i in range(self.a - self.c + 1):
                countx = 0
                counto = 0

                for k in range(self.c):
                    if self.n[i + k][j] == 1:
                        countx += 1
                    if self.n[i + k][j] == 2:
                        counto += 1

                if countx == self.c:
                    self.winner = self.p1
                    self.Looser = self.p2
                    self.game_over = True
                    self.save_result()
                    return True

                if counto == self.c:
                    self.winner = self.p2
                    self.Looser = self.p1
                    self.game_over = True
                    self.save_result()
                    return True

        # diagonal \
        for i in range(self.a - self.c + 1):
            for j in range(self.a - self.c + 1):
                countx = 0
                counto = 0

                for k in range(self.c):
                    if self.n[i + k][j + k] == 1:
                        countx += 1
                    if self.n[i + k][j + k] == 2:
                        counto += 1

                if countx == self.c:
                    self.winner = self.p1
                    self.Looser = self.p2
                    self.game_over = True
                    self.save_result()
                    return True

                if counto == self.c:
                    self.winner = self.p2
                    self.Looser = self.p1
                    self.game_over = True
                    self.save_result()
                    return True

        # diagonal /
        for i in range(self.a - self.c + 1):
            for j in range(self.c - 1, self.a):
                countx = 0
                counto = 0

                for k in range(self.c):
                    if self.n[i + k][j - k] == 1:
                        countx += 1
                    if self.n[i + k][j - k] == 2:
                        counto += 1

                if countx == self.c:
                    self.winner = self.p1
                    self.Looser = self.p2
                    self.game_over = True
                    self.save_result()
                    return True

                if counto == self.c:
                    self.winner = self.p2
                    self.Looser = self.p1
                    self.game_over = True
                    self.save_result()
                    return True

        return False


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    game = Game(player1, player2, 3, 3, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game.wincond(screen, None):
            pygame.time.wait(1500)
            pygame.quit()
            exit()

        pygame.display.update()
        clock.tick(60)