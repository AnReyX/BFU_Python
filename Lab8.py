import os
import random
import csv

path = input("Input the file path: ")
if not path:
  path = os.path.join(os.getcwd(), "data.csv")
  with open(path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City", "Emoji", "Bool"])
    for _ in range(10):
      name = random.choice(["Антон", "Андрей", "Алиса", "Александр", "Аня", None])
      age = random.randint(2, 80)
      city = random.choice(["Москва", "Калининград", "Санкт-Петербург", "Город", "Город Героев", None])
      emoji = random.choice([":)", ":3", "owo", "uwu", ":D", None])
      bool_value = random.choice([True, False])
      writer.writerow([name, age, city, emoji, bool_value])
with open(path, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]


def show(write_style="top", length=5, separator=" "):
    global data
    if len(data) < length:
      print(f"Not enough info to output! Amount resized.")
      length = len(data)

    if write_style == "top":
        for i in range(length):
          print(separator.join([str(data[i][k]) for k in data[i]]))
    elif write_style == "bottom":
        for i in range(len(data) - length, len(data)):
          print(separator.join([str(data[i][k]) for k in data[i]]))
    elif write_style == "random":
        for i in random.sample(range(len(data)), length):
          print(separator.join([str(data[i][k]) for k in data[i]]))


def info():
  print(f"{len(data)}x{len(data[0])}")
  for key in data[0]:
      count = 0
      type_value = "str"
      type_found = False
      for row in data:
          if row[key]:
              count += 1
              if type_found:
                  continue
              if row[key] in ["True", "False"]:
                  type_value = "bool"
                  type_found = True
              elif row[key].isdigit():
                  type_value = "int"
                  type_found = True
      print(f"{key} {count} {type_value}")


def DelNaN():
  global data
  data = [row for row in data if all(row.values())]
  print("Deleted rows with empty data.")


def MakeDS():
  cwd_workdata = os.path.join(os.getcwd(), "workdata")
  os.makedirs(cwd_workdata, exist_ok=True)
  os.makedirs(os.path.join(cwd_workdata, "Learning"), exist_ok=True)
  os.makedirs(os.path.join(cwd_workdata, "Testing"), exist_ok=True)
  train_amount = round(len(data) * 0.7)
  test_amount = len(data) - train_amount
  data_copy = data.copy()
  random.shuffle(data_copy)
  with open(os.path.join(cwd_workdata, "Learning", "train.csv"), "w", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data_copy[:train_amount]:
      writer.writerow(row)
  with open(os.path.join(cwd_workdata, "Testing", "test.csv"), "w", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    for row in data_copy[train_amount:]:
      writer.writerow(row)


info()
DelNaN()
info()
MakeDS()
show("bottom", 10, ",")