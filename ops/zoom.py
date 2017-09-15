from skimage import transform
import numpy as np
import re
import cv2

PREFIX = 'zoom'
REGEX = re.compile(r"^" + PREFIX + "_(?P<p1x>[-0-9]+)_(?P<p1y>[-0-9]+)_(?P<p2x>[-0-9]+)_(?P<p2y>[-0-9]+)")
PAD_VALUE = 0

class Zoom:
    def __init__(self, p1x, p1y, p2x, p2y):
        self.p1x = p1x
        self.p1y = p1y
        self.p2x = p2x
        self.p2y = p2y
        self.code = PREFIX + str(p1x) + '_' + str(p1y) + '_' + str(p2x) + '_' + str(p2y)

    def process(self, img):
      
        height, width = img.shape[:2]
        res = cv2.resize(img,(int(1.2*width), int(1.2*height)), interpolation = cv2.INTER_AREA)
        dst = res[self.p1y:int(self.p2y*height/100), self.p1x:int(self.p2x*width/100)]
        # Crop from x, y, w, h -> 100, 200, 300, 400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

        return dst

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Zoom(int(d['p1x']), int(d['p1y']), int(d['p2x']), int(d['p2y']))