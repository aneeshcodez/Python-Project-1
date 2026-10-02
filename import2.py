import json
# Python Data -> Json

user = {
    "name" : "sam",
    "age" : 22
}

json_data = json.dumps(user)
print(user)
print(json_data)