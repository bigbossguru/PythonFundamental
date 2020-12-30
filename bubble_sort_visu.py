import pygame, sys, random

BLACK = (30, 30, 30)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 640
HEIGHT = 480

pygame.init()

screen_res = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(screen_res)
pygame.display.set_caption('Bubble Sort')
clock = pygame.time.Clock()

#Width and thickness of the bars
thickness_bar = 4
width_bar = WIDTH // thickness_bar

#The data array
height_arr = []

#State of each bar [1] is normal, [2] is solved, [0] is change
state = []

for i in range(width_bar):
    height = random.randint(10, 460)
    height_arr.append(height)
    state.append(1)

count = 0
#print(height_arr)

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

    if count < len(height_arr):
        for j in range(len(height_arr)-1-count):
            if height_arr[j] > height_arr[j+1]:
                state[j] = 0
                state[j+1] = 0
                tmp = height_arr[j]
                height_arr[j] = height_arr[j+1]
                height_arr[j+1] = tmp
            else:
                state[j] = 1
                state[j+1] = 1
    else: print('Done')
    count += 1
    
    #print(state)

    if len(height_arr)-count >= 0:
        state[len(height_arr)-count] = 2

    print(state)

    for i in range(len(height_arr)):
        if state[i] == 0:
            color = RED
        elif state[i] == 2:
            color = GREEN
        else:
            color = WHITE
        pygame.draw.rect(screen, color, pygame.Rect(thickness_bar*i, HEIGHT-height_arr[i], thickness_bar, height_arr[i]), 1)

    
    pygame.display.flip()
    clock.tick(10)
