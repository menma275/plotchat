# poetry run python main.py

from pyaxidraw import axidraw
from pysvg.structure import Svg
from pysvg.text import Text

from pysvg.shape import Rect, Circle, Line

from ollama import chat
from ollama import ChatResponse
import textwrap

# パラメータ設定
offsetX = 20
offsetY = 20
line_height = 7
font_size = 5
width = 210
height = 297
max_text_width = width - offsetX *2 

# 1文字あたりの幅（ざっくり）
char_width = font_size / 1.85
max_chars_per_line = int(max_text_width / char_width)

# モデル呼び出し
# model = "phi4"
# response: ChatResponse = chat(model=model, messages=[
#     {"role": "user", "content": "count up number upto 10"},
# ])

# raw_text = response["message"]["content"]

raw_text = "American logistics in the Western Allied invasion of Germany supported operations in Northwest Europe during World War II from January 1945 until the end of the war in Europe on 8 May. The Allies had to advance across the Rhineland, which was in the grip of thaws, rains and floods. They were then confronted by the Rhine, the most formidable barrier to the Allied advance since the English Channel. The river was crossed and bridged, and railways and pipelines were run across it. Most supplies were delivered by rail. In the final advance into the heart of Germany, combat losses and ammunition expenditure declined, while shortages of fuel and spare parts developed, as was to be expected in fast-moving mobile operations. Railheads were pushed forward, with the rehabilitation of the network keeping pace with the advance, while the Motor Transport Service organized an express service that moved supplies from the railheads to the forward units"

# 改行＋折り返し処理
wrapped_lines = []
for line in raw_text.splitlines():
    wrapped_lines.extend(textwrap.wrap(line, width=max_chars_per_line))

# SVG生成
svg = Svg(width=f"{width}mm", height=f"{height}mm")
for i, line in enumerate(wrapped_lines):
    y = offsetY + i * line_height
    text = Text(line, x=f"{offsetX}mm", y=f"{y}mm")
    text.set_font_family("Hiragino Sans")
    text.set_font_size(f"{font_size}mm")
    # svg.addElement(text)

rect = Rect(x=f"{offsetX}mm", y=f"{offsetY}mm", width="100mm", height="100mm", fill="red")

svg.addElement(rect)

ad = axidraw.AxiDraw()

ad.plot_setup(svg)

ad.plot_run()

# svg.save("test.svg", encoding='utf-8')
