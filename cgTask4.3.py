from PIL import Image, ImageFilter
import numpy as np
from scipy.ndimage import median_filter

img = Image.open('file1.png')

arrayImg = np.array(img)

noise = np.random.random(arrayImg.shape) > 0.9
arrayImg[noise] = 0
arrayImg[noise] = 255

noisedImg = Image.fromarray(arrayImg)
noisedImg.save('noisedImage4.3.jpeg')

denoisedArrayImg = median_filter(arrayImg, size=3)

denoisedImg = Image.fromarray(denoisedArrayImg)
denoisedImg.save('denoisedImage4.3.jpeg')