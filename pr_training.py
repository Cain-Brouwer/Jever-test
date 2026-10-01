from feature_extractor import extract_features
from sklearn.linear_model import LogisticRegression
from pr_data import data

features = []
labels = []

for pr in data.training.verzamel_trainings_data():
    added_lines, removed_lines = extract_features(pr)
    features.append((added_lines, removed_lines))
    labels.append(pr["is_merge_conflict"])



def train_model():
    model = LogisticRegression()
    model.fit(features, labels)
    return model