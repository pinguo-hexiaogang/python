import json

obj = {"name": "xiaogang", "age": 20, "houses": ["nanhu", "lushan"]}


jsonStr = json.dumps(obj)

print(jsonStr)
print(type(jsonStr))

jsonBean = json.loads(jsonStr)
print(jsonBean)
print(type(jsonBean))
