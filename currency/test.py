import json

with open('data', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
