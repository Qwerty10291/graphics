from PIL import Image, ImageFilter
import numpy as np
from scipy.ndimage import median_filter

img = Image.open('file1.png')

arrayImg = np.array(img)

noise_r = np.random.poisson(arrayImg[:, :, 0])
noise_g = np.random.poisson(arrayImg[:, :, 1])
noise_b = np.random.poisson(arrayImg[:, :, 2])

noisedArrayImg = np.stack((noise_r, noise_g, noise_b), axis=-1)

noisedImg = Image.fromarray(np.uint8(noisedArrayImg))

noisedImg.save('noisedImage4.2.jpeg')

# либо это

denoisedImg = noisedImg.filter(ImageFilter.MinFilter(3))
denoisedImg.save('denoisedImage4.2.jpeg')

# либо это

# denoised_img_array = median_filter(noisedArrayImg, size=3)
# denoised_img = Image.fromarray(np.uint8(denoised_img_array))
# denoised_img.save('denoisedImage4.2.jpeg')