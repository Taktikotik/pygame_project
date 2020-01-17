import pygame
import os

pygame.init()
size = width1, height1 = 500, 500
color = (255, 255, 255)
screen = pygame.display.set_mode(size)
page_count = 1
print('Пожалуйста, напишите номер уровня:')
level = int(input())
if level == 1:
    cell_places = [(4, 0),
                   (3, 1), (4, 1), (5, 1),
                   (2, 2),(3, 2), (4, 2), (5, 2), (6, 2),
                   (1, 3), (2, 3),(3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                   (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                   (1, 5), (4, 5), (7, 5),
                   (1, 6), (4, 6), (7, 6),
                   (1, 7),(2, 7), (3, 7), (4, 7), (7, 7),
                   (1, 8), (2, 8), (3, 8), (4, 8), (7, 8)]
elif level == 2:
    cell_places = [(4, 0), (5, 0), (6, 0),
                   (3, 1), (5, 1), (6, 1), (7, 1),
                   (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
                   (6, 2), (7, 2), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
                   (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4),
                   (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (9, 5), (10, 5), (11, 5),(12, 5), (13, 5),(14, 5), (15, 5),
                   (3, 6), (4, 6), (5, 6), (6, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6),
                   (15, 6), (16, 6), (17, 6), (18, 6), (19, 6),
                   (3, 7), (4, 7), (5, 7), (6, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7),
                   (15, 7), (16, 7), (17, 7), (18, 7), (19, 7),
                   (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (10, 9), (11, 9), (14, 9), (15, 9)]
else:
    pygame.quit()
    raise SystemExit('Ошибка: Такого уровня не существует.')


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 75
        self.top = 75
        self.cell_size = 20

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        screen.fill((0, 0, 0))
        colors = [(0, 0, 0), color, (100, 100, 255)]
        font = pygame.font.Font(None, 20)
        text1x = font.render('      3   4', 6, (100, 255, 100))
        text2x = font.render('1    6    2   2   9   4   3   6   1', 1, (100, 255, 100))
        text1y = font.render('1', 1, (100, 255, 100))
        text2y = font.render('3', 1, (100, 255, 100))
        text3y = font.render('5', 1, (100, 255, 100))
        text4y = font.render('7', 1, (100, 255, 100))
        text5y = font.render('9', 1, (100, 255, 100))
        text6y = font.render('1 1 1', 1, (100, 255, 100))
        text7y = font.render('1 1 1', 1, (100, 255, 100))
        text8y = font.render('4 1', 1, (100, 255, 100))
        text9y = font.render('4 1', 1, (100, 255, 100))

        screen.blit(text1x, (100, 40))
        screen.blit(text2x, (80, 60))
        screen.blit(text1y, (40, 80))
        screen.blit(text2y, (40, 100))
        screen.blit(text3y, (40, 120))
        screen.blit(text4y, (40, 140))
        screen.blit(text5y, (40, 160))
        screen.blit(text6y, (40, 180))
        screen.blit(text7y, (40, 200))
        screen.blit(text8y, (40, 220))
        screen.blit(text9y, (40, 240))

        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, colors[self.board[y][x]], (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell_coords):
        self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 3

    def way_to_finish(self):
        finish = True
        for y in range(self.height):
            for x in range(self.width):
                cell = (y, x)
                if (self.board[x][y] != 1 and cell in cell_places) or\
                    (self.board[x][y] == 1 and cell not in cell_places):
                    finish = False
        return finish


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def start_screen(page):
    if page == 1:
        intro_text = ["Правила игры nonogram:",
                      'Вы должны закрашивать клетки',
                      'в которых точно уверены.',
                      'В итоге вы увидете зашифрованную картинку.',
                      'Каждое число, это число закрашенных',
                      'подряд клеток.',
                      'для переключения между страницами правил',
                      'нажимайте стрелочки']

    elif page == 2:
        intro_text = ["Правила игры nonogram:",'Мы знаем длину блока, но',
                      'не всегда знаем его позицию.',
                      'Между блоками должна быть',
                      'как минимум одна пустая клетка.',
                      'чёрные клетки - не закрашенные клетки',
                      'белые клетки - закрашенные клетки',
                      'синие клетки - клетки в которых,',
                      'как вы думаете, не нужны для решения',]

    fon = pygame.transform.scale(load_image('fon1.jpg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        global event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()


def fin_screen():
    intro_text = ['Спасибо, что играли в мою игру!','','','','']
    fon = pygame.transform.scale(load_image('fon2.jpg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        global event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()

if level == 1:
    board = Board(9, 9)
elif level == 2:
    board = Board(20, 20)

start_screen(page_count)
while True:
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        break
    elif event.key == pygame.K_RIGHT and page_count < 2:
        page_count += 1
    elif event.key == pygame.K_LEFT and page_count > 1:
        page_count -= 1
    start_screen(page_count)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render()
    if board.way_to_finish():
        running = False
    pygame.display.flip()
fin_screen()
