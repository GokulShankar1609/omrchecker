import cv2

def detect_bubbles(thresh_img):
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bubbles = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > 100]
    return bubbles
