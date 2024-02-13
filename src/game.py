# importing libraries
import pygame
import time
import random

snake_speed = 10
size = 20

# Window size
window_x = 30 * size
window_y = 20 * size

# defining colors
black = pygame.Color(0, 0, 0)
dark = pygame.Color(12, 12, 12)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()


# Initialise game window
pygame.display.set_caption('Git_tutorial')
icon = pygame.image.load('../assets/game/icon.png')
pygame.display.set_icon(icon)
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [5 * size, 6 * size]

# defining first 4 blocks of snake body
snake_body = [[5 * size, 6 * size],
			[4 * size, 6 * size],
			[3 * size, 6 * size],
			[2 * size, 6 * size]
			]
# fruit position
fruit_position = [random.randrange(1, (window_x//size)) * size,
				random.randrange(1, (window_y//size)) * size]

fruit_spawn = True

# Load sprites
sheet = pygame.image.load('../assets/game/spritesheet.png').convert()
#lansa = pygame.image.load('../assets/game/tulepera.jpeg')
#lansa = pygame.transform.scale(lansa, (size, size))

rect = pygame.Rect((0, 192, 64, 64)) 
apple_sp = pygame.Surface(rect.size).convert()
apple_sp.blit(sheet, (0, 0), rect)
apple_sp = pygame.transform.scale(apple_sp, (size, size))

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# draw function (snake and apple) 
def draw():
    # draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], size, size))

    # draw apple
    #pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], size, size))
    game_window.blit(apple_sp, (fruit_position[0], fruit_position[1]))
    #game_window.blit(lansa, (fruit_position[0], fruit_position[1]))


# displaying Score function
def show_score(color, font, size):

    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():

    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()

def luis_lansa():
    lansa = pygame.image.load('../assets/game/tulepera.jpeg')

    pygame.display.set_caption('Luis Lansa')
    game_window = pygame.display.set_mode((lansa.get_width(), lansa.get_height()))
    
    while True:
        game_window.blit(lansa, (0, 0))
        pygame.display.update()
# Main Function
while True:
	
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

	# Moving the snake
    if direction == 'UP':
        snake_position[1] -= size
    if direction == 'DOWN':
        snake_position[1] += size
    if direction == 'LEFT':
        snake_position[0] -= size
    if direction == 'RIGHT':
        snake_position[0] += size

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
		
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//size)) * size, random.randrange(1, (window_y//size)) * size]
		
    fruit_spawn = True
    game_window.fill(dark)

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-size:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-size:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
	
    # Draw
    draw()

    # displaying score countinuously
    show_score(white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)

