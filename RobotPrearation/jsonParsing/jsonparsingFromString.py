import json

# What does the json.loads() method do in Python?

# Explain that json.loads() is used to parse a JSON string into a Python dictionary (or a list, depending on the JSON structure).
class Json:
    def parseJsonData(self):
        json_stirng = '{"1":"one", "2":"two", "3":"three", "4":"four"}'
        data = json.loads(json_stirng)
        print(data)
        print(data["1"])
        print(data["2"])

j = Json()
j.parseJsonData()