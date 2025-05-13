# poetry run python main.py
from plotchat.ai import aiResponse
from plotchat.svg import shapedText
import subprocess

txt = "txt.svg"
output = "output.svg"

user_input = input("Type anything:")
res = aiResponse(user_input)

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
