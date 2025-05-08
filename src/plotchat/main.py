# poetry run python main.py

from pysvg.structure import Svg
from pysvg.shape import Rect
from pysvg.text import Text

from ollama import chat
from ollama import ChatResponse

offsetX = "20mm"
offsetY = "20mm"

response: ChatResponse = chat(model="phi4", messages=[
    {
        "role": "user",
        "content": "count up number upto 10",
    }
])

res = response["message"]["content"]
print(res)

svg = Svg(width="210mm", height="297mm")
text = Text(res, x=offsetX, y=offsetY)
text.set_font_family("Hiragino Sans")
text.set_font_size("5mm")
svg.addElement(text)

svg.save("test.svg")
