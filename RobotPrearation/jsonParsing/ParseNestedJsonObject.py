import json

class ParseNestedJsonObject:
    def parseNestedObject(self):
        json_data = '{"user": {"name": "John", "details": {"age": 30}}}'
        data = json.loads(json_data)
        print(data['user']['details']['age'])

nestedJson = ParseNestedJsonObject()
nestedJson.parseNestedObject()
