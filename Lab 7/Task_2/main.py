import json

with open("ex_2.json") as f:
    data = json.load(f)

result = {el["name"]: el["phoneNumber"] for el in data}
print(result)