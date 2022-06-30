import cv2
def NoPicture():
    img = cv2.VideoCapture(0)
    active = True
    while active:
        ret, frame =img.read()
        cv2.imwrite("You're Wrong.png", frame)
        active = False
    img.release()
    cv2.destroyAllWindows()
NoPicture()