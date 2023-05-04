# importing libraries
import pygame
import time
import random
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Imnotgay100", port=5432)
cur = conn.cursor()

# Create user and user_score tables if they don't exist
cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(255) UNIQUE)")
cur.execute("CREATE TABLE IF NOT EXISTS user_score (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id), score INTEGER)")

# Get user input for username
username = input("Enter your username: ")
cur.execute("SELECT id FROM users WHERE username=%s", (username,))
user = cur.fetchone()
if user:
    user_id = user[0]
    print("Welcome back!")
    # TODO: Show current level
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    print("Welcome to the game!")

#initialize
pygame.init()

#color in rgb
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 102)

#screen setting
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 12

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

#function to show level
def Level(level):
        level_show = score_font.render("Level: " + str(int(level)), True, (100, 100, 255))
        screen.blit(level_show, [0, 50])

# to display score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

#snake drawing
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

#blitting final message (either play again or quit)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def save_score(score):
    cur.execute("INSERT INTO user_score (user_id, score) VALUES (%s, %s)", (user_id, score))
    conn.commit()
    print("Score saved!")

#main loop
def game_loop():
    game_over = False
    game_close = False
    
    # coordinates for snake. dx, dy - direction
    x1, y1 = screen_width/2, screen_height/2
    dx, dy = 0, 0
    
    snake_list = []
    length_of_snake = 1
    level_number = 1.0
    
    #locating food randomly
    foodx = round(random.randrange(0, screen_width-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, screen_height-snake_block)/10.0)*10.0
    
    while not game_over:
        
        #final scene
        while game_close == True:
            screen.fill(white)
            message("You Lost! Press Q-quit or C-Play again", red)
            Your_score(length_of_snake-1)
            pygame.display.update()
            
            #exit options
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        save_score(length_of_snake-1)
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
              
        #movements of snake by keyboard          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(length_of_snake-1)
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0
                elif event.key == pygame.K_RIGHT:
                    dy = 0
                    dx = snake_block
                elif event.key == pygame.K_LEFT:
                    dy = 0
                    dx = -snake_block
        
        #game over if snake goes outside of screen    
        if x1 >= screen_width or x1<0 or y1<0 or y1>=screen_height:
            game_close = True
        
        #capturing snakes movements    
        x1 += dx
        y1 += dy
        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        #game over if snake bites itself    
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        
        #functions to draw snake, display score and level
        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)
        Level(level_number)
        
        pygame.display.update()
        
        #drawing new food if previos was ate
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width-snake_block)/10.0)*10.0
            foody = round(random.randrange(0, screen_height-snake_block)/10.0)*10.0
            length_of_snake += 1
            level_number += 0.3
            
        #speed of snake (fps)
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()

game_loop()