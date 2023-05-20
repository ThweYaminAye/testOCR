from pytesseract import pytesseract
from PIL import Image
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_Text(img_name):
    image = Image.open(img_name)
    text = pytesseract.image_to_string(image)
    return text
output = get_Text("two.jpg")
print(output)


