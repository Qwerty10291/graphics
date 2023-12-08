import numpy as np
from PIL import Image

def contrast_enhancement(image_path, factor):
    img = Image.open(image_path)

    img_array = np.array(img)

    enhanced_img_array = np.clip(img_array * factor, 0, 255).astype(np.uint8)
    enhanced_img = Image.fromarray(enhanced_img_array)
    enhanced_img.save("contast.png")

def linear_contrast(image_path):
    image = np.array(Image.open(image_path).convert('RGB'))
    for i in range(3):
        min_val = np.min(image[:, :, i])
        max_val = np.max(image[:, :, i])
        image[:, :, i] = ((image[:, :, i] - min_val) / (max_val - min_val)) * 255

    converted = Image.fromarray(np.uint8(image))
    converted.save('contrast.png')

def solarize(image_path, threshold):
    img = Image.open(image_path)
    img_array = np.array(img)
    img_solarized = np.where(img_array < threshold, 255 - img_array, img_array)
    img_result = Image.fromarray(img_solarized.astype(np.uint8))
    img_result.save("contrast.png")

def logariphmic(image_path, scale_factor):
    image = np.array(Image.open(image_path).convert('RGB'))
    image = (scale_factor * np.log(1 + image / 255)) * 255
    converted = Image.fromarray(np.uint8(image))
    converted.save('contrast.png')


if __name__ == "__main__":
    # Путь к изображению
    image_path = "file1.png"

    cont_type = input("введите тип преобразования(1 - препарированием, 2 - линейный, 3 - соляризация, 4 - логарифмическое изменение яркости)")

    if cont_type == "1":
        contrast_factor = 1.5
        contrast_enhancement(image_path, contrast_factor)
    elif cont_type == "2":
        linear_contrast(image_path)
    elif cont_type == "3":
        solarize(image_path, 100)
    elif cont_type == "4":
        logariphmic(image_path, 1.4)
