from skimage import transform
import re
import numpy as np
import cv2

PREFIX = 'rot'
REGEX = re.compile(r"^" + PREFIX + "_(?P<angle>-?[0-9]+)")

class Rotate:
    def __init__(self, angle):
        self.angle = angle
        self.code = PREFIX + str(angle)

    def process(self, img):
        #return transform.rotate(img, -self.angle)
        rows,cols,ch = img.shape

        #M = np.float32([[1,0,2],[0,1,4]])
        #dst = cv2.warpAffine(img,M,(cols,rows))

        M = cv2.getRotationMatrix2D((cols/2,rows/2),self.angle,1.0)
        dst = cv2.warpAffine(img,M,(cols,rows))

        return(dst)

    @staticmethod
    def match_code(code):
        match = REGEX.match(code)
        if match:
            d = match.groupdict()
            return Rotate(int(d['angle']))
