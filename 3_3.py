from PIL import Image, ImageDraw
import numpy as np

def koch(draw, order, size, position, angle=0):
    if order == 0:
        # рисуем отрезок
        end_x = position[0] + size * np.cos(np.radians(angle))
        end_y = position[1] + size * np.sin(np.radians(angle))
        draw.line([position, (end_x, end_y)], fill="black", width=2)
    else:
        # рекурсивно рисуем три отрезка Коха
        size /= 3.0
        koch(draw, order - 1, size, position, angle)
        position = (position[0] + size * np.cos(np.radians(angle)),
                    position[1] + size * np.sin(np.radians(angle)))
        koch(draw, order - 1, size, position, angle - 60)
        position = (position[0] + size * np.cos(np.radians(angle - 60)),
                    position[1] + size * np.sin(np.radians(angle - 60)))
        koch(draw, order - 1, size, position, angle + 60)
        position = (position[0] + size * np.cos(np.radians(angle + 60)),
                    position[1] + size * np.sin(np.radians(angle + 60)))
        koch(draw, order - 1, size, position, angle)

def fractal_dimension(image:Image.Image):
    # Расчет фрактальной размерности по покрытию

    total_pixels = 0
    covered_pixels = 0

    for i in range(image.width):
        for j in range(image.height):
            total_pixels += 1
            if image.getpixel((i, j)) != (255, 255, 255):  # Если пиксель не белый
                covered_pixels += 1

    fractal_dimension = covered_pixels / total_pixels
    return fractal_dimension

# Параметры кривой Коха
order = 4
size = 600

# Создание изображения и рисование кривой Коха
image = Image.new("RGB", (600, 200), "white")
draw = ImageDraw.Draw(image)
start_position = (0, 180)
koch(draw, order, size, start_position)
print("Фрактальная размерность:", fractal_dimension(image))

# Сохранение изображения
image.save("koch_snowflake.png")