# ShoeDesign Pro v3.2

AI-Powered Ethical Footwear Design Platform

## Features
- Tkinter GUI + AI trend prediction (Torch)
- Biomech optimization (PuLP)
- Sustainability LCA (Sympy)
- Supply chain traceability (NetworkX + blockchain stub)
- 3D parametric renders (Matplotlib)
- Full unit tests & Docker support

## Run Locally
```bash
pip install -r requirements.txt
python app.py

mkdir static
echo "# Generated files\nThis folder contains runtime-generated images (3D renders, supply chain viz, etc.)\nDo not edit files here manually." > static/README.md
