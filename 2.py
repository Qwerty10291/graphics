import pygame
from pygame.locals import QUIT
import sys

points1 = [(50, 50), (100, 150), (150, 50), (20, 10), (70, 40)]
points2 = [(260, 50), (300, 50), (340, 75), (360, 120), (310, 100), (280, 150)]
points3 = [(450, 50), (490, 30), (550, 120), (470, 150)]
points4 = [(650, 50), (710, 30), (710, 80), (750, 100), (700, 90), (680, 150), (700, 60)]

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Polygon Filling')

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_contour(points):
    if len(points) > 1:
        pygame.draw.lines(screen, BLACK, True, points)

def fill_polygon_1(points):
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    scan_lines = list(range(min_y, max_y + 1))

    for scan_line in scan_lines:
        intersections = []
        for i in range(len(points)):
            j = (i + 1) % len(points)
            x1, y1 = points[i]
            x2, y2 = points[j]

            if (y1 < scan_line <= y2) or (y2 < scan_line <= y1):
                x = int(x1 + (scan_line - y1) / (y2 - y1) * (x2 - x1))
                intersections.append(x)

        intersections.sort()
        for k in range(0, len(intersections), 2):
            start_x = intersections[k]
            end_x = intersections[k + 1]
            pygame.draw.line(screen, BLACK, (start_x, scan_line), (end_x, scan_line))

def fill_polygon_2(x, y, points):
    if len(points) < 3:
        return

    stack = [(x, y)]
    filled_pixels = set()

    while stack:
        current_point = stack.pop()

        if is_inside_polygon(current_point, points):
            filled_pixels.add(current_point)

            pygame.draw.rect(screen, BLACK, (*current_point, 1, 1))

            neighbors = [
                (current_point[0], current_point[1] - 1),
                (current_point[0], current_point[1] + 1),
                (current_point[0] - 1, current_point[1]),
                (current_point[0] + 1, current_point[1])
            ]

            stack.extend(neighbor for neighbor in neighbors if neighbor not in filled_pixels)

def fill_polygon_3(x, y, points):
    if len(points) < 3:
        return

    stack = [(x, y)]
    filled_rows = set([y])

    while stack:
        current_point = stack.pop()

        pygame.draw.rect(screen, BLACK, (*current_point, 1, 1))

        right_point = (current_point[0] + 1, current_point[1])
        while is_inside_polygon(right_point, points):
            pygame.draw.rect(screen, BLACK, (*right_point, 1, 1))
            right_point = (right_point[0] + 1, right_point[1])

        left_point = (current_point[0] - 1, current_point[1])
        while is_inside_polygon(left_point, points):
            pygame.draw.rect(screen, BLACK, (*left_point, 1, 1))
            left_point = (left_point[0] - 1, left_point[1])

        new_y = current_point[1] + 1
        if new_y not in filled_rows:
            flag = True
            for i in range(right_point[0] - 1, left_point[0] + 1, -1):
                if is_inside_polygon((i, new_y), points):
                    if flag:
                        stack.append((i, new_y))
                    flag = False
                else:
                    flag = True
            filled_rows.add(new_y)

        new_y = current_point[1] - 1
        if new_y not in filled_rows:
            flag = True
            for i in range(right_point[0] - 1, left_point[0] + 1, -1):
                if is_inside_polygon((i, new_y), points):
                    if flag:
                        stack.append((i, new_y))
                    flag = False
                else:
                    flag = True
            filled_rows.add(new_y)

def fill_polygon_4(surface:pygame.surface.Surface,  points):
    max_x = max(p[0] for p in points)

    j = len(points) - 1

    for i in range(len(points)):
        if points[i][1] != points[j][1]:
            for y in range(min(points[i][1], points[j][1]), max(points[i][1], points[j][1])):
                new_x = int(points[i][0] + (y - points[i][1]) / (points[j][1] - points[i][1]) * (points[j][0] - points[i][0]))
                for x in range(new_x, max_x):
                    if surface.get_at((x, y)).r == 0:
                        surface.set_at((x, y), WHITE)
                    else:
                        surface.set_at((x, y), BLACK)

        j = i

def is_inside_polygon(point, polygon):
    x, y = point
    inside = False
    j = len(polygon) - 1

    for i in range(len(polygon)):
        if ((polygon[i][1] > y) != (polygon[j][1] > y)) and \
           (x < (polygon[j][0] - polygon[i][0]) * (y - polygon[i][1]) / (polygon[j][1] - polygon[i][1]) + polygon[i][0]):
            inside = not inside
        j = i

    return inside

screen.fill(WHITE)
draw_contour(points1)
draw_contour(points2)
draw_contour(points3)

# Fill polygons using different methods
fill_polygon_1(points1)
fill_polygon_2(261, 51, points2)
fill_polygon_3(470, 50, points3)
fill_polygon_4(screen, points4)
draw_contour(points4)
pygame.display.flip()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    clock.tick(30)