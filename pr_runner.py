from feature_extractor import extract_features
from sklearn.linear_model import LogisticRegression
from pr_data import data
from kans_checker import list_loop

predictions = []
features = []
labels = []

for pr in data.training:
    added_lines, removed_lines = extract_features(pr)
    features.append((added_lines, removed_lines))
    labels.append(pr["is_merge_conflict"])

model = LogisticRegression()
model.fit(features, labels)

resultant = model.predict_proba(features)[:, 1]
result = list_loop(resultant)

new_pr3 = extract_features(data.trainings_data.pr_data3(self=data.trainings_data()))
new_pr4 = extract_features(data.test_data.pr_data4(self=data.test_data()))
new_pr5 = extract_features(data.test_data.pr_data5(self=data.test_data()))
new_pr6 = extract_features(data.test_data.pr_data6(self=data.test_data()))

pr_result3 = model.predict_proba([new_pr3])[:, 1]
pr_result4 = model.predict_proba([new_pr4])[:, 1]
pr_result5 = model.predict_proba([new_pr5])[:, 1]
pr_result6 = model.predict_proba([new_pr6])[:, 1]

print(pr_result3)
print(pr_result4)
print(pr_result5)
print(pr_result6)

print(model.coef_)
print(model.intercept_)

actual_label = data.trainings_data.pr_data3(self=data.trainings_data())["is_merge_conflict"]