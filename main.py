import pygame
import random

# Culori
Alb = (255, 255, 255)
Negru = (0, 0, 0)
Gri = (100, 100, 100)
Rosu = (255, 0, 0)
Albastru = (0, 0, 255)

class Text:
    def __init__(self, posx, posy, color, size):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.size = size
        self.Font = pygame.font.SysFont('timesnewroman.ttf',size)

    def draw(self, ecran, posx, posy, text):
        btn1 = self.Font.render(text, True, self.color)
        btn1Rect = btn1.get_rect()
        btn1Rect.center = (self.posx, self.posy)
        ecran.blit(btn1, btn1Rect)

def alegere():
    global x, y, Player, Rsp, Matrix, Ecran, Negru
    # Linia 1
    if x < 82 and y < 82 and Matrix[0][0] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [21, 21, 42, 42], 4)
            Player = False
            Matrix[0][0] = 1
        else:
            Player = True
            Matrix[0][0] = 2
            pygame.draw.line(Ecran, Negru, [27, 54], [54, 27], 4)
            pygame.draw.line(Ecran, Negru, [27, 27], [54, 54], 4)
    if 82 < x < 166 and y < 82 and Matrix[0][1] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [Latime // 3 + 23, 21, 42, 42], 4)
            Player = False
            Matrix[0][1] = 1
        else:
            Player = True
            Matrix[0][1] = 2
            pygame.draw.line(Ecran, Negru, [Latime // 3 + 30, 54], [Latime // 3 + 57, 27], 4)
            pygame.draw.line(Ecran, Negru, [Latime // 3 + 30, 27], [Latime // 3 + 57, 54], 4)
    if 166 < x < 250 and y < 82 and Matrix[0][2] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [Latime - Latime // 3 + 23, 21, 42, 42], 4)
            Player = False
            Matrix[0][2] = 1
        else:
            Matrix[0][2] = 2
            Player = True
            pygame.draw.line(Ecran, Negru, [Latime - Latime // 3 + 30, 27], [Latime - Latime // 3 + 57, 54], 4)
            pygame.draw.line(Ecran, Negru, [Latime - Latime // 3 + 30, 54], [Latime - Latime // 3 + 57, 27], 4)

    # Linia 2
    if x < 82 and 82 < y < 165 and Matrix[1][0] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [21, Latime // 3 + 23, 42, 42], 4)
            Player = False
            Matrix[1][0] = 1
        else:
            Player = True
            Matrix[1][0] = 2
            pygame.draw.line(Ecran, Negru, [27, Latime // 3 + 57], [54, Latime // 3 + 30], 4)
            pygame.draw.line(Ecran, Negru, [27, Latime // 3 + 30], [54, Latime // 3 + 57], 4)
    if 82 < x < 166 and 82 < y < 165 and Matrix[1][1] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [Latime // 3 + 23, Latime // 3 + 23, 42, 42], 4)
            Player = False
            Matrix[1][1] = 1
        else:
            Player = True
            Matrix[1][1] = 2
            pygame.draw.line(Ecran, Negru, [Latime // 3 + 30, Latime // 3 + 57], [Latime // 3 + 57, Latime // 3 + 30],
                             4)
            pygame.draw.line(Ecran, Negru, [Latime // 3 + 30, Latime // 3 + 30], [Latime // 3 + 57, Latime // 3 + 57],
                             4)
    if 166 < x < 250 and 82 < y < 165 and Matrix[1][2] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [Latime - Latime // 3 + 23, Latime // 3 + 23, 42, 42], 4)
            Player = False
            Matrix[1][2] = 1
        else:
            Player = True
            Matrix[1][2] = 2
            pygame.draw.line(Ecran, Negru, [Latime - Latime // 3 + 30, Latime // 3 + 57],
                             [Latime - Latime // 3 + 57, Latime // 3 + 30], 4)
            pygame.draw.line(Ecran, Negru, [Latime - Latime // 3 + 30, Latime // 3 + 30],
                             [Latime - Latime // 3 + 57, Latime // 3 + 57], 4)

    # Linia 3
    if x < 82 and 165 < y < 250 and Matrix[2][0] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [23, Latime - Latime // 3 + 23, 42, 42], 4)
            Player = False
            Matrix[2][0] = 1
        else:
            Player = True
            Matrix[2][0] = 2
            pygame.draw.line(Ecran, Negru, [30, Latime - Latime // 3 + 57], [57, Latime - Latime // 3 + 30], 4)
            pygame.draw.line(Ecran, Negru, [30, Latime - Latime // 3 + 30], [57, Latime - Latime // 3 + 57], 4)
    if 82 < x < 166 and 165 < y < 250 and Matrix[2][1] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [Latime // 3 + 23, Latime - Latime // 3 + 23, 42, 42], 4)
            Player = False
            Matrix[2][1] = 1
        else:
            Player = True
            Matrix[2][1] = 2
            pygame.draw.line(Ecran, Negru, [Latime // 3 + 30, Latime - Latime // 3 + 57],
                             [Latime // 3 + 57, Latime - Latime // 3 + 30], 4)
            pygame.draw.line(Ecran, Negru, [Latime // 3 + 30, Latime - Latime // 3 + 30],
                             [Latime // 3 + 57, Latime - Latime // 3 + 57], 4)
    if 166 < x < 250 and 165 < y < 250 and Matrix[2][2] > 2:
        if Player:
            pygame.draw.ellipse(Ecran, Negru, [Latime - Latime // 3 + 23, Latime - Latime // 3 + 23, 42, 42], 4)
            Player = False
            Matrix[2][2] = 1
        else:
            Player = True
            Matrix[2][2] = 2
            pygame.draw.line(Ecran, Negru, [Latime - Latime // 3 + 30, Latime - Latime // 3 + 57],
                             [Latime - Latime // 3 + 57, Latime - Latime // 3 + 30], 4)
            pygame.draw.line(Ecran, Negru, [Latime - Latime // 3 + 30, Latime - Latime // 3 + 30],
                             [Latime - Latime // 3 + 57, Latime - Latime // 3 + 57], 4)

def start():
    global Exit
    Exit = False
    global Rsp
    Ecran.fill(Negru)
    while not Exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if 92 > x > 35 and 130 > y > 117:
                    Exit = True
                    Rsp = False
                if 155 < x < 215 and 130 > y > 117:
                    Exit = True
                    Rsp = True
        Buton1P.draw(Ecran, Buton1P.posx, Buton1P.posy, '1 Player')
        Buton2P.draw(Ecran, Buton2P.posx, Buton2P.posy, '2 Playeri')
        pygame.display.flip()



pygame.init()
pygame.font.init()

# Ecran
Inaltime = Latime = 250
Ecran = pygame.display.set_mode((Latime, Inaltime))
pygame.display.set_caption('TicTacToe')

# Butoane:
Buton1P = Text(Latime//3 - 20, Inaltime//2, Alb, 22)
Buton2P = Text(Latime - Latime//3 + 20, Inaltime//2, Alb, 22)
Textfinal = Text(Latime//2, 50, Albastru, 35)
ButonExit = Text(Latime//3 - 20, 80, Albastru, 22)
ButonRetry = Text(Latime - Latime//3, 80, Albastru, 22)


Matrix = [[5, 6, 7], [8, 9, 10], [30, 12, 13]]

Player = True
Exit = False
Exit2 = False
Exitfinal = False
Exxit = False
Rsp = False
Win = 0
ceas = pygame.time.Clock()

start()
while not Exxit:
        Ecran.fill(Alb)
        # Linii:
        pygame.draw.line(Ecran, Negru, [0, Latime // 3], [Latime, Latime // 3], 4)
        pygame.draw.line(Ecran, Negru, [0, Latime - Latime // 3], [Latime, Latime - Latime // 3], 4)
        pygame.draw.line(Ecran, Negru, [Latime // 3, 0], [Latime // 3, Latime], 4)
        pygame.draw.line(Ecran, Negru, [Latime - Latime // 3, 0], [Latime - Latime // 3, Latime], 4)
        while not Exit2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit2 = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        x = pos[0]
                        y = pos[1]
                        alegere()
                elif not Rsp and not Player:
                    while not Player:
                        x = random.randrange(249)
                        y = random.randrange(249)
                        alegere()

            pygame.display.flip()
            # Col1
            if Matrix[0][0] == Matrix[1][0] == Matrix[2][0]:
                pygame.draw.line(Ecran, Negru, [Latime // 6, Latime//12],
                                 [Latime // 6, Latime - Latime // 12 - 2], 4)
                Win = Matrix[0][0]
                break
            # Lin 1
            elif Matrix[0][0] == Matrix[0][1] == Matrix[0][2]:
                pygame.draw.line(Ecran, Negru, [Latime // 12, Latime // 6],
                                 [Latime - Latime // 12 + 2, Latime // 6], 4)
                Win = Matrix[0][0]
                break
            # Diag Prin
            elif Matrix[0][0] == Matrix[1][1] == Matrix[2][2]:
                pygame.draw.line(Ecran, Negru, [27, 27],
                                 [Latime - Latime//3 + 57, Latime - Latime//3 + 57], 4)
                Win = Matrix[0][0]
                break
            # Lin 2
            elif Matrix[1][0] == Matrix[1][1] == Matrix[1][2]:
                pygame.draw.line(Ecran, Negru, [Latime // 12, Latime // 6 + Latime//3 + 2],
                                 [Latime - Latime // 12 + 2, Latime // 6 + Latime//3 + 2], 4)
                Win = Matrix[1][0]
                break
            # Lin 3
            elif Matrix[2][0] == Matrix[2][1] == Matrix[2][2]:
                pygame.draw.line(Ecran, Negru, [Latime // 12, Latime -Latime // 6 + 2],
                                 [Latime - Latime // 12 + 2, Latime -Latime // 6 + 2], 4)
                Win = Matrix[2][0]
                break
            # Col 2
            elif Matrix[0][1] == Matrix[1][1] == Matrix[2][1]:
                pygame.draw.line(Ecran, Negru, [Latime // 6 + Latime//3 + 2, Latime // 12],
                                 [Latime // 6 + Latime//3 + 2, Latime - Latime // 12 - 2], 4)
                Win = Matrix[0][1]
                break
            # Col 3
            elif Matrix[0][2] == Matrix[1][2] == Matrix[2][2]:
                pygame.draw.line(Ecran, Negru, [Latime - Latime // 6 + 2, Latime // 12],
                                 [Latime - Latime // 6 + 2, Latime - Latime // 12 - 2], 4)
                Win = Matrix[2][0]
                break
            # Diag sec
            elif Matrix[0][2] == Matrix[1][1] == Matrix[2][0]:
                pygame.draw.line(Ecran, Negru, [30, Latime - Latime//3 + 57], [Latime - Latime // 3 + 57, 27], 4)
                Win = Matrix[2][0]
                break

            gata = False
            for i in range(3):
                for j in range(3):
                    if Matrix[i][j] > 2:
                        gata = True
                        break
                if gata:
                    break
            if not gata:
                break
            ceas.tick(60)


        print(Win, Matrix)



        pygame.draw.rect(Ecran, Gri, [47, ButonExit.posy - 11.75, 33, 20])
        pygame.draw.rect(Ecran, Gri, [129, ButonRetry.posy - 11.75, 77, 20])
        ButonExit.draw(Ecran, ButonExit.posx, ButonExit.posy, 'Exit')
        ButonRetry.draw(Ecran, ButonRetry.posx, ButonRetry.posy, 'New game')

        if Win == 1:
            pygame.draw.rect(Ecran, Gri, [25, Textfinal.posy - 11, 200, 25])
            Textfinal.draw(Ecran, Textfinal.posx, Textfinal.posy, 'Player 1 Winner!')
        elif Win == 2:
            pygame.draw.rect(Ecran, Gri, [25, Textfinal.posy - 12.5, 200, 25])
            Textfinal.draw(Ecran, Textfinal.posx, Textfinal.posy, 'Player 2 Winner!')
        else:
            pygame.draw.rect(Ecran, Gri, [45, Textfinal.posy - 12.5, 160, 27])
            Textfinal.draw(Ecran, Textfinal.posx, Textfinal.posy, 'No Winner :(')

        pygame.display.flip()
        Player = False

        while not Exitfinal:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exitfinal = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    if 48 < x <77 and 70 < y < 85:
                        Exitfinal = True
                    if 130 < x < 203 and 68 < y < 87:
                        start()
                        Win = 0
                        Matrix = [[5, 6, 7], [8, 9, 10], [30, 12, 13]]
                        Player = True
                        break
            if Player:
                break

            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if 48 < x <77 and 70 < y < 85:
                ButonExit.color = Rosu
                ButonExit.draw(Ecran, ButonExit.posx, ButonExit.posy, 'Exit')
                pygame.display.flip()
            else:
                ButonExit.color = Albastru
                ButonExit.draw(Ecran, ButonExit.posx, ButonExit.posy, 'Exit')
                pygame.display.flip()
            if 130 < x < 203 and 68 < y < 87:
                ButonRetry.color = Rosu
                ButonRetry.draw(Ecran, ButonRetry.posx, ButonRetry.posy, 'New game')
                pygame.display.flip()
            else:
                ButonRetry.color = Albastru
                ButonRetry.draw(Ecran, ButonRetry.posx, ButonRetry.posy, 'New game')
                pygame.display.flip()

        if Exitfinal:
            break

pygame.quit()
