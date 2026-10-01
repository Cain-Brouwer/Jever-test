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

# print(f"Features: {features}")
# print(f"Labels: {labels}")

model = LogisticRegression()
model.fit(features, labels)

resultant = model.predict_proba(features)[:, 1]
result = list_loop(resultant)

# print(resultant)
# print(result)

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


# test gedeelte
# ____________________________________________________________________________

pr_result3_float = pr_result3[0]
pr_result4_float = pr_result4[0]
pr_result5_float = pr_result5[0]
pr_result6_float = pr_result6[0]


def classify_probability(probability):
    if probability < 0.5:
        return False
    else:
        return True

# def pr_checker(pr):
#     for pr in

pr_output3 = classify_probability(pr_result3_float)
pr_output4 = classify_probability(pr_result4_float)
pr_output5 = classify_probability(pr_result5_float)
pr_output6 = classify_probability(pr_result6_float)

print(actual_label)

comparison = pr_output3 == actual_label
print(comparison)
