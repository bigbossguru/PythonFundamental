import pygame, sys

def bouncong_rect():
    global x_speed, y_speed, other_speed
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    rgb_color = [255,255,255]

    if moving_rect.right >= width or moving_rect.left <= 0:
        x_speed *= -1

    if moving_rect.bottom >= height or moving_rect.top <= 0:
        y_speed *= -1

    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= height:
        other_speed *= -1

    collision_tolernce = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolernce and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolernce and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolernce and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolernce and x_speed > 0:
            x_speed *= -1
    pygame.draw.rect(screen, rgb_color, moving_rect)
    pygame.draw.rect(screen, (255,0,0), other_rect)

width, height = 800, 800
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))

moving_rect = pygame.Rect(350,350,50,50)
x_speed, y_speed = 5, 4
other_rect = pygame.Rect(300,600,200,100)
other_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    bouncong_rect()
    pygame.display.flip()
    clock.tick(60)
