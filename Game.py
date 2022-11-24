# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la computación
# Graficas por computadora

# Maria Isabel Solano

# Imports 
import pygame
import time

# Important data
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# Game class
class Game(object):
    def __init__(self, screen, filename):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen

        cells_x = int(self.width / 10)
        cells_y = int(self.width / 10)

        self.cells = [[False for i in range(cells_y)] for x in range(cells_x)]

        self.load_inital_game(filename)


    def point(self, x, y):
        self.screen.set_at((x, y), WHITE)

    def draw_cell(self, x, y):
        0

    def load_inital_game(self, filename):
        info = []

        with open(filename) as f:
            for line in f.readlines():
                info.append(list(line))


        for i in range(len(info)):
            for j in range(len(info[i])):
                if info[i][j] == '1':
                    self.cells[i][j] = True
                if info[i][j] == '0':
                    self.cells[i][j] = False
                # else ignore
                    


pygame.init()
screen = pygame.display.set_mode((400, 400))
g = Game(screen, './first_gen.txt')

running = True
while running:

    screen.fill(BLACK)

    

    pygame.display.flip()
    
    time.sleep(2)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
