def extract_features(pr_data):
    code_diffs = pr_data["code_diffs"]
    code_diffs = code_diffs.splitlines()
    added_lines = 0
    removed_lines = 0
    for diffs in code_diffs:
        if diffs.startswith('+') and not diffs.startswith('+++'):
            added_lines += 1
            print(f"Added line: {diffs[1:]}")
        elif diffs.startswith('-') and not diffs.startswith('---'):
            removed_lines += 1
            print(f"Removed line: {diffs[1:]}")
    return added_lines, removed_lines
