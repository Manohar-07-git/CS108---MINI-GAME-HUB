import pygame
import sys
import numpy as np

pygame.init()

width = 600
height = 600
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 30)

p1 = sys.argv[1]
p2 = sys.argv[2]


class Game:
    def __init__(self, a, b, size):
        self.p1 = a
        self.p2 = b
        self.turn = 1
        self.board = np.zeros((size, size))

    def switch(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1


class TicTacToe(Game):
    def __init__(self, a, b):
        super().__init__(a, b, 9)

    def draw(self):
        screen.fill((255, 255, 255))
        gap = width // 9

        for i in range(10):
            pygame.draw.line(screen, (0, 0, 0), (0, i * gap), (width, i * gap))
            pygame.draw.line(screen, (0, 0, 0), (i * gap, 0), (i * gap, height))

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 1:
                    pygame.draw.circle(screen, (255, 0, 0), (j * gap + gap//2, i * gap + gap//2), 12)
                if self.board[i][j] == 2:
                    pygame.draw.circle(screen, (0, 0, 255), (j * gap + gap//2, i * gap + gap//2), 12)

        pygame.display.update()

    def check(self, player):
        b = self.board

        for i in range(9):
            for j in range(5):
                if np.all(b[i, j:j+5] == player):
                    return True
                if np.all(b[j:j+5, i] == player):
                    return True

        for i in range(5):
            for j in range(5):
                if np.all(np.diag(b[i:i+5, j:j+5]) == player):
                    return True
                if np.all(np.diag(np.fliplr(b[i:i+5, j:j+5])) == player):
                    return True

        return False

    def play(self):
        run = True
        gap = width // 9

        while run:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    r = y // gap
                    c = x // gap

                    if self.board[r][c] == 0:
                        self.board[r][c] = self.turn

                        if self.check(self.turn):
                            run = False
                        else:
                            self.switch()

            if np.all(self.board != 0):
                run = False

        pygame.time.delay(1000)


def menu():
    run = True

    while run:
        screen.fill((200, 200, 200))
        t = font.render("Press 1 for TicTacToe | 2 to Quit", True, (0, 0, 0))
        screen.blit(t, (100, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    g = TicTacToe(p1, p2)
                    g.play()
                if event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()


menu()
