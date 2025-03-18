import csv
import json


def writeExample():
    with open("input.json", "w") as f:
        fruits = ['apple', 'pear', 'banana']
        veggies = ['tomato', 'cucumber', 'potato']
        f.write(json.dumps({'fruits': fruits, 'veggies': veggies}))


writeExample()
try:
    json_name = input("Input file name (*.json): ")
    csv_name = input("Output file name (*.csv): ")
    if not csv_name.endswith(".csv"):
        raise FileNotFoundError
        data = json.load(json_file)
    with open(f"{json_name.rstrip('.json')}.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=" ", quotechar=",")
        writer.writerows(data.items())
    with open(f"{json_name.rstrip('.json')}.csv") as csv_read:
        reader = csv.reader(csv_read)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Error! Wrong file name.")