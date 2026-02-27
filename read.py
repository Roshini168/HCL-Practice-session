import json
d={"name": "Jenifer",
    "age":  20,
    "department": "Computer Science",
    "marks": 85}
with open("student.json", "w") as f:
    json.dump(d, f, indent=4)

with open("student.json","r") as f:
    a=json.load(f)
    print(a["age"])
