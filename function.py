import cv2

def process_image(image):
    img_obj = cv2.imread(image)
    return cv2.cvtColor(img_obj, cv2.COLOR_BGR2GRAY)