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
GRAY  = ( 25,  25,  25)

# Game class
class Game(object):
    def __init__(self, screen, filename):
        _, _, self.width, self.height = screen.get_rect()
        self.screen = screen

        self.cells_x = int(self.width / 10) # amount of cells on x axis
        self.cells_y = int(self.width / 10) # amount of cells on y axis

        self.cells_width = int(self.width / self.cells_x)
        self.cells_height = int(self.height / self.cells_x)

        self.cells = [[False for i in range(self.cells_y)] for x in range(self.cells_x)]

        self.load_inital_game(filename)
        self.render_cells()


    def point(self, x, y, c = WHITE):
        self.screen.set_at((y, x), c)

    def draw_cell(self, x, y):
        for i in range(self.cells_width):
            for j in range(self.cells_height):
                self.point(
                    int(i + x*self.cells_width),
                    int(j + y*self.cells_height)
                    )

    def render_cells(self):
        # cells
        for i in range(len(self.cells)):
            for j in range(len(self.cells)):
                if self.cells[i][j]:
                    self.draw_cell(i, j)

        # grid
        for i in range(self.width):
            if i%self.cells_width == 0:
                for j in range(self.height):
                    self.point(j, i, GRAY)
        for i in range(self.height):
            if i%self.cells_height == 0:
                for j in range(self.width):
                    self.point(i, j, GRAY)
                

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

    def iteration(self):
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                0
                    


pygame.init()
screen = pygame.display.set_mode((400, 400))
g = Game(screen, './first_gen.txt')

running = True
while running:

    screen.fill(BLACK)
    g.render_cells()

    pygame.display.flip()
    
    time.sleep(2)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
