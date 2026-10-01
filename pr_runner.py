from pr_training import train_model
from pr_tests import test_model

def run_model():
    trained_model = train_model()
    test_model(trained_model)


run_model()