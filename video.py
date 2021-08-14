import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    # if frame is read correctly
    if not isTrue:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow('Video', frame)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()