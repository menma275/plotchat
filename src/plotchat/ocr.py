import os
from PIL import Image
import sys
import pyocr
import pyocr.builders

import easyocr

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

print("Using OCR tool:", tool.get_name())
# print("Available languages:", tool.get_available_languages())

basedir = os.path.abspath(os.path.dirname(__file__))
img_path = os.path.join(basedir, "../../img/3.jpeg")

# reader = easyocr.Reader(['en'], gpu=False)
# txt_array = reader.readtext(img_path, detail=0)
# txt = ''.join(txt_array)


img = Image.open(img_path).convert("L")
threshold = 90 
binary = img.point(lambda x: 255 if x > threshold else 0, '1')
binary.save('binary.jpg')
txt = tool.image_to_string(
        binary, 
        # lang="jpn+eng", 
        # lang="jpn", 
        lang="eng", 
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print(txt)

