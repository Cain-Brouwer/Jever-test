from dummy_predicter import dummy_predicter
from dummy_predicter import pr_all
from feature_extractor import extract_features
from kans_checker import list_loop
from sklearn.linear_model import LogisticRegression

predictions = []
features = []
labels = []

for pr in pr_all:
    prediction = dummy_predicter(pr)
    predictions.append(prediction)
    added_lines, removed_lines = extract_features(pr)
    features.append((added_lines, removed_lines))
    labels.append(pr["is_merge_conflict"])

result = list_loop(predictions)

print(f"All predictions are valid probabilities: {result}")
print(f"Features: {features}")
print(f"Labels: {labels}")

model = LogisticRegression()
model.fit(features, labels)

resultant = model.predict_proba(features)

print(resultant)