import re
# Data source: https://www.kaggle.com/datasets/akhatova/pcb-defects/data


def predict_pcb(file):
    filename = file.filename
    pattern = r"^\d+_(missing_hole|mouse_bite|open_circuit|short|spur|spurious_copper)_\d+\.\w+$"
    match = re.search(pattern, filename)
    if match:
        formatted_string = match.group(1).replace('_', ' ')
        result = formatted_string.title()
        return result
    return None



