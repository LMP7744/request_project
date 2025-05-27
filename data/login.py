import json
def get_data(file_path):
    test_data = []
    with open(file_path, 'r',encoding='utf-8') as f:
        json_data = json.load(f)
        for i in json_data:
            test_data.append(tuple(i.values()))
    return test_data
