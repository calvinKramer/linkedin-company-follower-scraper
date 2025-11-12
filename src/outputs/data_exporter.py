thonimport json

def export_data(data):
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)