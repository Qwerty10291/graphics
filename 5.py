import time
import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Геометрические преобразования")

rect_width, rect_height = 100, 50
rect_color = WHITE
rect_x, rect_y = (WIDTH - rect_width) // 2, (HEIGHT - rect_height) // 2
rect_angle = 0  # Угол поворота
rect_scale = 1  # Масштаб
flip_x = False
flip_y = False
last_flip = time.time()

clock = pygame.time.Clock()

def draw_rectangle(flip_x:bool, flip_y:bool):
    rotated_rect = pygame.transform.rotate(rect, rect_angle)
    scaled_rect = pygame.transform.scale(rotated_rect, (int(rect_width * rect_scale), int(rect_height * rect_scale)))
    if flip_x or flip_y:
        scaled_rect = pygame.transform.flip(scaled_rect, flip_x, flip_y)
    screen.blit(scaled_rect, (rect_x, rect_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= 5
    if keys[pygame.K_RIGHT]:
        rect_x += 5
    if keys[pygame.K_UP]:
        rect_y -= 5
    if keys[pygame.K_DOWN]:
        rect_y += 5
    if keys[pygame.K_w]:
        rect_angle += 5
    if keys[pygame.K_s]:
        rect_angle -= 5
    if keys[pygame.K_a]:
        rect_scale *= 1.1
    if keys[pygame.K_d]:
        rect_scale /= 1.1
    if keys[pygame.K_q]:
        if time.time() - last_flip > 0.1:
            flip_x = not flip_x
            last_flip = time.time()
    if keys[pygame.K_e]:
        if time.time() - last_flip > 0.1:
            flip_y = not flip_y
            last_flip = time.time()

    screen.fill(BLACK)
    rect = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    pygame.draw.rect(rect, rect_color, (0, 0, rect_width, rect_height))
    draw_rectangle(flip_x, flip_y)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()