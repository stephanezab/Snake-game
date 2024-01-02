import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display size
WIN_WIDTH = 600
WIN_HEIGHT = 400

# Initialize display
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Snake Game by Pythonista')

clock = pygame.time.Clock()

SNAKE_BLOCK = 10
SNAKE_SPEED = 10

font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 25)

# Function to display the score of the player
# def your_score(score):
#     value = score_font.render("Your Score: " + str(score), True, yellow)
#     WIN.blit(value, [0, 0])

# # Function to draw the snake
# def our_snake(SNAKE_BLOCK, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(WIN, black, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])

def draw(snake_list, score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    WIN.blit(value, [0, 0])

    for x in snake_list:
        pygame.draw.rect(WIN, black, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])

# Function to display messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    WIN.blit(mesg, [WIN_WIDTH / 6, WIN_HEIGHT / 3])

def gameLoop():  # main game loop
    game_over = False
    game_close = False

    x1 = WIN_WIDTH / 2
    y1 = WIN_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Randomly place food item
    foodx = round(random.randrange(0, WIN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, WIN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            WIN.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            #your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= WIN_WIDTH - SNAKE_BLOCK or x1 < 0 or y1 >= WIN_HEIGHT- SNAKE_BLOCK or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        WIN.fill(blue)
        pygame.draw.rect(WIN, green, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x[0] == snake_Head[0] and x[1] == snake_Head[1]:
                game_close = True

        # our_snake(SNAKE_BLOCK, snake_List)
        # your_score(Length_of_snake - 1)

        draw(snake_List, Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIN_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, WIN_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()
