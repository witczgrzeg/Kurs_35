import json

with open('data.json', 'r') as file:
    data = json.loads(file.read())
    print(data)
    print(type(data))

with open('data.json', 'w') as file:
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    file.write(json.dumps(data))
