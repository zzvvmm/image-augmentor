from skimage.filters import gaussian
from skimage.exposure import rescale_intensity
import re
import cv2
import numpy as np
import colorsys
from PIL import Image


CODE = 'colour'
REGEX = re.compile(r"^" + CODE + "_(?P<sigma>[.0-9]+)")

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

class Colour:
    def __init__(self, sigma):
        self.code = CODE + str(sigma)
        self.sigma = sigma
    def shift_hue(arr, hout):
        r, g, b, a = np.rollaxis(arr, axis=-1)
        h, s, v = rgb_to_hsv(r, g, b)
        h = hout
        r, g, b = hsv_to_rgb(h, s, v)
        arr = np.dstack((r, g, b, a))
        return arr
    def process(self, img2):
        image = img2.convert('RGBA')
        arr = np.array(np.asarray(image).astype('float'))
        new_img2 = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')
        return new_img2
      

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Colour(float(d['sigma']))
