from PIL import Image, ImageDraw
import math

def draw_circle_bresenham(image, center, radius):
    x, y = center
    d = 3 - 2 * radius
    draw = ImageDraw.Draw(image)

    x = 0
    y = radius

    while x <= y:
        plot_points(draw, x, y, center)
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        plot_points(draw, x, y, center)


def draw_circle_midpoint(image, center, radius):
    x, y = center
    draw = ImageDraw.Draw(image)
    p = 1 - radius
    x, y = 0, radius

    plot_points(draw, x, y, center)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plot_points(draw, x, y, center)

def draw_circle_approximate(image, center, radius):
    num_segments = 100
    angle = 2 * math.pi / num_segments

    # Координаты вершин многоугольника, аппроксимирующего окружность
    x_coords = [center[0] + radius * math.cos(i * angle) for i in range(num_segments + 1)]
    y_coords = [center[1] + radius * math.sin(i * angle) for i in range(num_segments + 1)]

    for i in range(0, num_segments):
        bresenham_line(image, round(x_coords[i]), round(y_coords[i]), round(x_coords[i + 1]), round(y_coords[i + 1]))


def plot_points(draw, x, y, center):
    draw.point([center[0] + x, center[1] + y], fill="black")
    draw.point([center[0] - x, center[1] + y], fill="black")
    draw.point([center[0] + x, center[1] - y], fill="black")
    draw.point([center[0] - x, center[1] - y], fill="black")
    draw.point([center[0] + y, center[1] + x], fill="black")
    draw.point([center[0] - y, center[1] + x], fill="black")
    draw.point([center[0] + y, center[1] - x], fill="black")
    draw.point([center[0] - y, center[1] - x], fill="black")

def bresenham_line(image, x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx

    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = 0
    y = y0
    y_step = 1 if y0 < y1 else -1

    for x in range(x0, x1 + 1):
        coord = (y, x) if steep else (x, y)
        image.putpixel(coord, (0, 0, 0))

        error += dy
        if 2 * error >= dx:
            y += y_step
            error -= dx

# Create a blank white image
width, height = 400, 400
image = Image.new("RGB", (width, height), "white")

# Set the center and radius of the circle
center = (width // 2, height // 2)
radius = 100

# Draw the circle on the image
draw_circle_approximate(image, center, radius)

# Save the image to a file (optional)
image.save("circle.png")