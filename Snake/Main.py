__author__ = 'Z50-70'

import pygame
import Levels
from Snake import *
from random import randint

SNAKE_SIZE = 20
BLOCK_SIZE = 20
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 360
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Snake')
window.fill((0, 0, 0))
screen = pygame.Surface((WINDOW_WIDTH - BLOCK_SIZE * 2, WINDOW_HEIGHT - BLOCK_SIZE * 2))

# отрисовка стен
x, y = 0, 0
for line in Levels.level_1:
    for i in line:
        if i == '_':
            pygame.draw.rect(window, (255, 0, 0),
                             ((x * BLOCK_SIZE, y * BLOCK_SIZE), ((x + 1) * BLOCK_SIZE, (y + 1) * BLOCK_SIZE)))
        x += 1
    y += 1
    x = 0

snake_block = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
snake = Snake()

food_block = pygame.Surface((SNAKE_SIZE, SNAKE_SIZE))
food_block.fill((255, 255, 0))

# отрисовка змейки на старте
temp = snake.head
while temp != None:
    snake_block.fill((randint(50, 200), randint(50, 200), randint(50, 200)))
    screen.blit(snake_block, (temp.x * SNAKE_SIZE, temp.y * SNAKE_SIZE))
    temp = temp.next
window.blit(screen, (BLOCK_SIZE, BLOCK_SIZE))
pygame.display.update()

# ожидание нажатия любой клавиши перед стартом
temp = True
while temp:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            temp = False

direction = 'down'
mainLoop = True
while mainLoop:

    # перехват нажатий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'down':
                    direction = 'up'
            if event.key == pygame.K_DOWN:
                if direction != 'up':
                    direction = 'down'
            if event.key == pygame.K_LEFT:
                if direction != 'right':
                    direction = 'left'
            if event.key == pygame.K_RIGHT:
                if direction != 'left':
                    direction = 'right'

    #добавление куска в начало
    if direction == 'up':
        snake.add((snake.head.x, snake.head.y - 1))
    if direction == 'down':
        snake.add((snake.head.x, snake.head.y + 1))
    if direction == 'left':
        snake.add((snake.head.x - 1, snake.head.y))
    if direction == 'right':
        snake.add((snake.head.x + 1, snake.head.y))

    #проверка на еду
    if not (snake.head.x == 3 and snake.head.y == 3):
        snake.delete()

    #проверка на выход за пределы поля
    if snake.head.x >= (screen.get_width() / SNAKE_SIZE) or snake.head.x < 0 or snake.head.y >= (
                screen.get_height() / SNAKE_SIZE) or snake.head.y < 0:
        print('Game Over')
        print('Your score: ', len(snake))
        break

    #проверка на столкновение с собой
    temp = snake.tail
    while temp.prev != None:
        if snake.head.x == temp.x and snake.head.y == temp.y:
            print('Game over')
            print('Your score: ', len(snake))
            mainLoop = False
        temp = temp.prev

    #отрисовка змейки
    screen.fill((0, 0, 0))
    screen.blit(food_block, (60, 60))
    temp = snake.head
    while temp != None:
        snake_block.fill((randint(50, 200), randint(50, 200), randint(50, 200)))
        screen.blit(snake_block, (temp.x * SNAKE_SIZE, temp.y * SNAKE_SIZE))
        temp = temp.next

    window.blit(screen, (BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()
    pygame.time.delay(150)
pygame.quit()
input()