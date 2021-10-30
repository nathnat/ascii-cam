import cv2

# La liste des charactères du moins au plus plein
ASCII_CHARS = '.,:;+*?%S#@'

capture = cv2.VideoCapture(0)

while True:
    isTrue, image = capture.read()

    # Si l'image est lu correctement
    if not isTrue:
        print("Pas d'accès à la webcam...")
        break

    # On redimensionne l'image grâce a un produit en croix
    width = 120
    height = int(width * image.shape[0] / image.shape[1])
    dim = (width, height)

    image = cv2.resize(image, dim)

    # On rend l'image en noir et blanc
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # On transforme l'image en ASCII art
    result = ""
    i_save = 0
    for i in range(gray.shape[0]):
        for j in range(gray.shape[1]):

            result += ASCII_CHARS[round(gray[i][j] / (255 / len(ASCII_CHARS))) - 1]

            if (i_save != i):
                i_save = i
                result += "\n"

    # On print le résultat
    print(result)
