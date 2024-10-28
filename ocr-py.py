import pytesseract
from PIL import Image

image = Image.open('/Users/shaojie/Desktop/1.png')
text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)
