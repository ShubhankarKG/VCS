from difflib import unified_diff


def get_differences(file_1, file_2):
    with open(file_1) as f1:
        f1_text = f1.read()
    with open(file_2) as f2:
        f2_text = f2.read()
    list_of_changes = []
    for line in unified_diff(f1_text, f2_text, fromfile=file_1, tofile=file_2, lineterm=" "):
        list_of_changes.append(line)
    return list_of_changes
