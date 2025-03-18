import csv
import sys
import json


def writeExample():
    with open("input.json", "w") as f:
        fruits = ['apple', 'pear', 'banana']
        veggies = ['tomato', 'cucumber', 'potato']
        f.write(json.dumps({'fruits': fruits, 'veggies': veggies}))


# writeExample()
try:
    name = sys.argv
    if len(name) != 2:
        name = input("Input file name: ").strip(".json")
    else:
        name = sys.argv[1].strip(".json")
    with open(f"{name}.json") as json_file:
        data = json.load(json_file)
    with open(f"{name}.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        for i in data.keys():
            writer.writerow([i] + data[i])
    with open(f"{name}.csv") as csv_read:
        reader = csv.reader(csv_read)
        for row in reader:
            print(row)
        print(f"Result written to {name}.csv!")
except FileNotFoundError:
    print("Error! Wrong file name.")
