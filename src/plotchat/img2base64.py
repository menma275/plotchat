import asyncio
import numpy as np
import cv2
import base64
from io import BytesIO
from PIL import Image

async def imgBase64(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pil_img = Image.fromarray(img_rgb)

    buffer = BytesIO()
    pil_img.save(buffer, format="PNG")  # or "JPEG"
    buffer.seek(0)

    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # data_url = f"data:image/png;base64,{img_base64}"
    
    return img_base64
