import cv2 as cv
import numpy as np
from numpy.lib.type_check import imag

def transform(img):

    # Get width and height of the image
    height, width, _ = img.shape

    result = ""
    x_save = 0
    for x in range(height):
        for y in range(width):

            # Récupération des données RGB du pixel
            r = img[x, y, 2]
            g = img[x, y, 1]
            b = img[x, y, 0]

            # Calcul de l'intensité
            intensity = 0.2126 * r + 0.7152 * g + 0.0722 * b

            char = "";
            if intensity > 200: char = '.'
            elif intensity > 175: char = ','
            elif intensity > 150: char = ';'
            elif intensity > 125: char = 'c'
            elif intensity > 100: char = 'k'
            elif intensity > 75: char = 'U'
            elif intensity > 50: char = 'B'
            elif intensity > 25: char = '#'
            else: char = ' '

            result += char

            if x != x_save:
                result += "\n"
                x_save = x

    return result

blank = np.zeros((500,500,3), dtype='uint8')

# 5. Write text
cv.putText(blank, "caca\ncaca", (0,5), cv.FONT_HERSHEY_TRIPLEX, 0.4, (0,255,0), 1)
cv.imshow('Text', blank)

cv.waitKey(0)