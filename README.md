# PlotChat

**Chat with AI, using real pen and paper.**

PlotChat brings a uniquely tangible experience to AI interaction. Write a note by hand, and the system captures it, lets an AI formulate a response, and then physically writes it back to you with a pen plotter.

It's a conversation that blends the warmth of analog handwriting with the power of artificial intelligence.

## How It Works

1.  **Capture:** The system captures an image of your handwritten note using a webcam or an ESP32-CAM.
2.  **OCR:** The image is processed using Optical Character Recognition (OCR) to extract the text.
3.  **AI Response:** The extracted text is sent to a local AI (Ollama) to generate a thoughtful response.
4.  **SVG Conversion:** The AI's response is converted into an SVG (Scalable Vector Graphics) file, essentially creating a digital version of the handwriting.
5.  **Plotting:** The generated SVG file is then meticulously plotted onto paper using an AxiDraw pen plotter, bringing the AI's response to life.

To start the process, simply run the main script:

```bash
poetry run python src/plotchat/main.py
```

## Requirements

This system requires the following tools:

- **Inkscape:** For processing SVG files.
  - Installation: `brew install inkscape`
  - Path setup: `sudo ln -s /Applications/Inkscape.app/Contents/MacOS/inkscape /usr/local/bin/inkscape`
- **Ollama:** For running the local AI.
  - Installation: `brew install ollama`
- **AxiDraw CLI:** For controlling the pen plotter.
  - Installation: See the [official documentation](https://axidraw.com/doc/cli_api/#introduction).
- **Tesseract:** For OCR.
  - Installation: `brew install tesseract` and `brew install tesseract-lang`
