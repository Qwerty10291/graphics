import random
from PIL import Image

def barnsley_fern(iterations) -> Image.Image:
    x, y = 0, 0
    image = Image.new("RGB", (800, 800), "white")

    for _ in range(iterations):
        r = random.uniform(0, 100)
        if r < 1:
            x, y = 0, 0.16 * y
        elif r < 86:
            x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 93:
            x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

        # Масштабирование координат в изображение
        ix, iy = int(400 + x * 80), int(800 - y * 80)
        
        # Закрашивание пикселя
        image.putpixel((ix, iy), (0, 128, 0))
    
    return image


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

if __name__ == "__main__":
    iterations = 100000  # Количество итераций для построения папоротника
    image = barnsley_fern(iterations)

    fractal_dimension_value = fractal_dimension(image)
    image.save("fern.png")
    print(f"Фрактальная размерность по покрытию: {fractal_dimension_value}")
