from pr_data import pr_data1, pr_data2

pr_all = [pr_data1(), pr_data2()]


def dummy_predicter(pr_data):
    return 0.1


output = dummy_predicter(pr_data1())

