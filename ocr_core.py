try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import os


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    tresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
   
    text = pytesseract.image_to_string(Image.open(tresh))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

