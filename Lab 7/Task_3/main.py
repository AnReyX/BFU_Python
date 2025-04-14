import json

with open("ex_3.json") as f:
    data = json.load(f)

to_add = [{"id": 3,
          "total": 300.00,
          "items": [
              {"name": "item 4",
               "quantity": 3,
               "price": 100.00}
          ]},
          {"id": 4,
           "total": 500.00,
           "items": [
               {"name": "item 5",
                "quantity": 5,
                "price": 50},
               {"name": "item 6",
                "quantity": 2,
                "price": 100},
               {"name": "item 7",
                "quantity": 1,
                "price": 50}
           ]
          }]
data["invoices"] += to_add

with open("new_3.json", "w") as f:
    json.dump(data, f, indent=4)