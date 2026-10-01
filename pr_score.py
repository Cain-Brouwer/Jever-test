import math
from pr_training import train_model, added_lines

def score_berekening():
    trained_model = train_model()
    trained_model.coef_
    trained_model.intercept_[0]

    features = (4, 0)

    added_lines_score = features[0]
    removed_lines_score = features[1]

    coefficient_added = trained_model.coef_[0][0]
    coefficient_removed = trained_model.coef_[0][1]

    score = (coefficient_added * added_lines_score) + (coefficient_removed * removed_lines_score) + trained_model.intercept_[0]
    return score

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

print(sigmoid(score_berekening()))