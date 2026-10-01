from feature_extractor import extract_features
from pr_data import data


def classify_probability(probability):
    if probability < 0.5:
        return False
    else:
        return True

def test_model(model):
    test_data = data.test.verzamel_test_data()
    for pr in test_data:
        added_lines, removed_lines = extract_features(pr)
        features = (added_lines, removed_lines)
        print(f"Testing PR: {pr['pr_id']}, Features: {features}")
        pr_result = model.predict_proba([features])[:, 1]
        pr_result_float = pr_result[0]
        pr_output = classify_probability(pr_result_float)
        print(f"PR: {pr['pr_id']}, Probability: {pr_result_float}, Classified as Merge Conflict: {pr_output}")
        comparison = pr_output == pr["is_merge_conflict"]
        print(f"Comparison with actual label: {comparison}")