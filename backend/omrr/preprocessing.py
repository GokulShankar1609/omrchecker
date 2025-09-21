import cv2

def preprocess_image(img_path: str):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Image not found: {img_path}")
    _, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh
