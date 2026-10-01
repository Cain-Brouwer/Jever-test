from feature_extractor import extract_features
from pr_data import data

def classify_probability(probability):
    if probability < 0.5:
        return False
    else:
        return True
