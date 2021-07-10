import pygame
import sys

# Описание окна игры
pygame.init()
sizeBlock = 100
margin = 15
width = height = sizeBlock*3 + margin*4

# Подключение размеров окна к библиотеке pygame
sizeWindow = (width,height)
screen = pygame.display.set_mode(sizeWindow)
pygame.display.set_caption("Крестики нолики")

# Описание цветов
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]

# Обработчик событий
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit():
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN():
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (sizeBlock + margin)
            row = y_mouse // (sizeBlock + margin)



    for row in range(3):
        for col in range(3):
            x = col*sizeBlock + (col + 1)*margin
            y = row*sizeBlock + (row + 1)*margin
            pygame.draw.rect(screen, white, (x, y, sizeBlock, sizeBlock))
    pygame.display.update()

