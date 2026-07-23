import pandas as pd
from sklearn.datasets import make_classification

def test_data_generation():
    """Simple test to verify we can generate synthetic data for testing."""
    X, y = make_classification(n_samples=10, n_features=4, random_state=42)
    assert X.shape == (10, 4)
    assert y.shape == (10,)
