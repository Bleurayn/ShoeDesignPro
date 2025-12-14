
## tests/test_core.py
```python
import pytest
import torch
from app import TrendPredictor, optimize_biomech, sustainability_score, viz_supply_chain, render_3d_shoe
import os

@pytest.fixture
def predictor():
    return TrendPredictor()

def test_trend_predictor(predictor):
    input_tensor = torch.tensor([[0.5]])
    probs = predictor(input_tensor)
    assert probs.shape == (1, len(predictor.linear.out_features))
    assert torch.isclose(probs.sum(), torch.tensor(1.0))  # Softmax sums to 1

def test_optimize_biomech():
    cushion = optimize_biomech(2.5, "flat")
    assert isinstance(cushion, float)
    assert cushion >= 0

def test_sustainability_score():
    materials = ["mycelium mesh", "algae rubber"]
    score = sustainability_score(materials)
    assert 0 <= score <= 10

def test_viz_supply_chain():
    png = viz_supply_chain()
    assert png == 'supply_chain.png'
    assert os.path.exists(png)  # File created

def test_render_3d_shoe():
    png = render_3d_shoe("ApexNova Sneaker")
    assert png == '3d_shoe.png'
    assert os.path.exists(png)

# GUI smoke test (no display needed for logic)
def test_gui_imports():
    from app import ShoeDesignGUI, tk
    assert tk  # Just check import
