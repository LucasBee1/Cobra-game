import pygame
import random

# inicializar o pygame
pygame.init()

# configuração da tela
width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Cobra")

# cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# configuração da cobra
snake_block = 10
snake_speed = 30

# configuração da maça
apple_block = 10

# fontes
font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/2, height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # posição da maça
    appleX = round(random.randrange(0, width - apple_block) / 10.0) * 10.0
    appleY = round(random.randrange(0, height - apple_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("Fim de jogo, pressione Q-Sair ou C-Jogar Novamente", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y
