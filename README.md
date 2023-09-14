# Nougat-GUI
GUI for the basic use of Facebook's [Nougat](https://github.com/facebookresearch/nougat). 
It basically uses OCR and AI to convert academic PDFs (like those published at Arxiv.org) into a type of text file called markdown, rendering any tables or math formulas in Mathpix Markdown-compatible format.

## To run:
- Install python.
- `python NougatGUI.py`
- If you don't have nougat installed, **it should install Nougat for you** the first time you run it.
- Nougat works faster with PyTorch: if you have a CUDA-enabled GPU, click on the link the app shows at the top to go to the PyTorch download page.
- Select Markdown compatibility checkbox if you want your output file to be in markdown style. The .mmd file generated can be treated like a regular markdown file: open it with any app that reads text.
- Select "Recompute" if there was an error while working on the same file and you want to start over from the beginning.
- To get more familiar, visit the [Nougat](https://github.com/facebookresearch/nougat) page.
