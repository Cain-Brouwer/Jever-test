from dummy_predicter import pr_all
from feature_extractor import extract_features
from sklearn.linear_model import LogisticRegression
from pr_data import pr_data3
from pr_data import pr_data4

from kans_checker import list_loop

predictions = []
features = []
labels = []

for pr in pr_all:
    added_lines, removed_lines = extract_features(pr)
    features.append((added_lines, removed_lines))
    labels.append(pr["is_merge_conflict"])

# print(f"Features: {features}")
# print(f"Labels: {labels}")

model = LogisticRegression()
model.fit(features, labels)

resultant = model.predict_proba(features)[:, 1]
result = list_loop(resultant)

# print(resultant)
# print(result)

new_pr3 = extract_features(pr_data3())
new_pr4 = extract_features(pr_data4())

pr_result3 = model.predict_proba([new_pr3])[:, 1]
pr_result4 = model.predict_proba([new_pr4])[:, 1]

print(pr_result3)
print(pr_result4)

print(model.coef_)
print(model.intercept_)

actual_label = pr_data3()["is_merge_conflict"]

pr_result3_float = pr_result3[0]
pr_result4_float = pr_result4[0]

def classify_probability(probability):
    if probability < 0.5:
        return False
    else:
        return True

pr_output3 = classify_probability(pr_result3_float)
print(pr_output3)

print(actual_label)

comparison = pr_output3 == actual_label
print(comparison)
