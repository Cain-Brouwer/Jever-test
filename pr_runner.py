from dummy_predicter import dummy_predicter
from dummy_predicter import pr_all
from kans_checker import list_loop

predictions = []

for pr in pr_all:
    prediction = dummy_predicter(pr)
    predictions.append(prediction)

result = list_loop(predictions)

print(f"All predictions are valid probabilities: {result}")