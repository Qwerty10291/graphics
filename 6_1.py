from PIL import Image
from random import randint

def draw_line_dda(image, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        image.putpixel((round(x), round(y)), (255, 255, 255))  # Белый цвет

        x += x_increment
        y += y_increment

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
        image.putpixel(coord, (255, 255, 255))

        error += dy
        if 2 * error >= dx:
            y += y_step
            error -= dx


if __name__ == "__main__":
    width, height = (int(n) for n in input("введите ширину и высоту изображения через пробел").split())
    img = Image.new("RGB", (width, height), (0, 0, 0))
    alg = input("введите алгоритм(1 - Брезенхэма, 2 - ЦДА)")

    for i in range(100):
        x1, x2 = randint(1, width - 1), randint(1, width - 1)
        y1, y2 = randint(1, height - 1), randint(1, height - 1)
        if alg == "1":
            bresenham_line(img, x1, y1, x2, y2)
        else:
            draw_line_dda(img, x1, y1, x2, y2)

    # Сохраняем изображение
    img.save("dda_line.png")