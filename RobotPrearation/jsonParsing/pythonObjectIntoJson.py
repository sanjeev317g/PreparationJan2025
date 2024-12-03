import json

# What does the json.dumps() method do in Python?

# Explain that json.dumps() converts a Python dictionary (or other objects) into a JSON string.
class PythonObjectIntoJson:
    def pythonObjectIntoJsonString(self):
        json_object = {"name": "Alice", "age": 25}
        data = json.dumps(json_object)
        print(data)
p = PythonObjectIntoJson()
p.pythonObjectIntoJsonString()