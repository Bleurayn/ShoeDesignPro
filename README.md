# ShoeDesign Pro v3.3

[![DOI](https://zenodo.org/badge/DOI/YOUR_DOI_HERE.svg)](https://doi.org/YOUR_DOI) <!-- After first release -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ultra-Enterprise AI-Powered Platform for Ethical, Personalized Footwear Design

## Features
- AI trend prediction & biomech optimization
- Sustainable material scoring
- 3D parametric renders & supply chain traceability
- Web dashboard (Flask + Bootstrap)
- Docker support & automated testing

## Quick Start
See [INSTRUCTIONS.txt](INSTRUCTIONS.txt) for setup steps.

## Live Demo
http://127.0.0.1:5000 (run locally)

## Contributing
Fork → Branch → PR welcome!

## License
MIT © 2025
## Run Locally
```bash

pip install -r requirements.txt
python app.py

## Project Structure
ShoeDesignPro/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # This file
├── LICENSE                     # MIT License
├── .gitignore                  # Git ignore rules
├── INSTRUCTIONS.txt            # Quick start guide
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD
├── templates/
│   └── index.html              # Web dashboard template
├── static/
│   └── README.md               # Note about runtime-generated files
└── tests/
└── test_core.py            # Pytest unit tests


Generated files (images, JSON) are created in `/static/` at runtime.
