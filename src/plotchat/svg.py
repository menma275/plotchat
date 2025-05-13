from pysvg.structure import Svg
from pysvg.text import Text

import textwrap

# Parameters of paper setting---
offsetX = 20
offsetY = 20
line_height = 7
font_size = 5
width = 210
height = 297
max_text_width = width - offsetX *2 

# a character witdth (approximate) ---
char_width = font_size / 1.85
max_chars_per_line = int(max_text_width / char_width)

def shapedText(res): 
    print("Now Writing 🖊️")
    wrapped_lines = []
    for line in res.splitlines():
        wrapped_lines.extend(textwrap.wrap(line, width=max_chars_per_line))

    # Generate SVG --- 
    svg = Svg(width=f"{width}mm", height=f"{height}mm")
    for i, line in enumerate(wrapped_lines):
        y = offsetY + i * line_height
        text = Text(line, x=f"{offsetX}mm", y=f"{y}mm")
        text.set_font_family("Hiragino Sans")
        text.set_font_size(f"{font_size}mm")
        svg.addElement(text)

    return svg
