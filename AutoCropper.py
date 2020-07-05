import numpy as np
from autocrop import Cropper
from PIL import Image

cropper = Cropper()
cropped_array = cropper.crop("/Users/srisagarkalisetty1/Downloads/Evelyn Vega_aligned.jpg")
cropped_image = Image.fromarray(cropped_array)
cropped_image.show()

