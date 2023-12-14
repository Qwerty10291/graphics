from PIL import Image, ImageFilter
import numpy as np

img = Image.open('file1.png')

arrayImg = np.array(img)

noise = np.random.random(arrayImg.shape) > 0.9
arrayImg[noise] = 0
arrayImg[noise] = 255

noisedImg = Image.fromarray(arrayImg)
noisedImg.save('noisedImage.jpeg')

denoisedImg = noisedImg.filter(ImageFilter.MinFilter(3))
denoisedImg.save('denoisedImage.jpeg')