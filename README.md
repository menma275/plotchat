# PlotChat

PlotChat is a system that captures text from an image, uses an AI to generate a response, and then plots the response using a pen plotter.

## Features

- Captures images from a local webcam or an ESP32-CAM.
- Performs OCR on the captured image to extract text.
- Uses a local AI (Ollama) to generate a response to the extracted text.
- Converts the AI's response into an SVG file.
- Plots the generated SVG file using the AxiDraw pen plotter.

## Requirements

This system requires the following tools:

### inkscape

- install
  - brew install inkscape
- set the path
  - sudo ln -s /Applications/Inkscape.app/Contents/MacOS/inkscape /usr/local/bin/inkscape

### ollama

- install
  - brew install ollama

### axicli

- install
  - https://axidraw.com/doc/cli_api/#introduction

### tesseract

- install
  - brew install tesseract
  - brew install tesseract-lang

## Usage

1. **Run the main script:**
   ```bash
   poetry run python src/plotchat/main.py
   ```

2. **How it works:**
   - The script captures an image.
   - It sends the image to an AI for OCR.
   - The recognized text is sent to another AI to get a response.
   - The response is converted to an SVG file (`output.svg`).
   - The SVG file is then plotted.
