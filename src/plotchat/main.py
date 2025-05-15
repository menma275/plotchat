# poetry run python main.py
import asyncio
from plotchat.ai import aiResponse
from plotchat.svg import shapedText
from plotchat.capture import capture
from plotchat.ocr import ocr 
from plotchat.ocr_ai import ocrAi 
from plotchat.img2base64 import imgBase64
import subprocess

async def main():
    lang = "Japanese"
    txt = "txt.svg"
    output = "output.svg"

# Capture and OCR
    img = capture()
    img_base64 = await imgBase64(img)
    user_input = await ocrAi(img_base64, lang)
# user_input = ocr(img)

# Receive text and Generate response
# user_input = input("Type anything: ")
    res = aiResponse(user_input, lang)

# Create svg from generated text
    svg = shapedText(res)
    svg.save(txt, encoding='utf-8')

# Covert text element into path
    text_to_path = [
        'inkscape',
        f'{txt}',
        f'--actions=select-all;object-to-path;export-filename:{output};export-do;'
        # '--actions=select-all;object-to-path;combine;union;export-filename:output.svg;export-do;'
        # '--actions=select-all;Extensions:AxiDraw Utilities/Hershey Text...;export-filename:output.svg;export-do;'
    ]
    result = subprocess.run(text_to_path, capture_output=True, text=True)

# Plot final result
    plot_text = [
        'axicli',
        f'{output}',
    ]
    result = subprocess.run(plot_text, capture_output=True, text=True)

asyncio.run(main())
