
# JSON
import json
data = {"name":"Sam", "age":20}
print(type(data))
with open("data.json", "w") as f:
    json.dump(data, f)
with open("data.json", "r") as f:
    data = json.load(f)



