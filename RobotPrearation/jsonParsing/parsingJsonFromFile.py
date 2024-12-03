import json

class jsonFromFile:
    def parsingFromFile(self):
        with open('RobotPrearation\\jsonParsing\\test.json', 'r') as file:
            data = json.load(file)
            print(data["lastName"])

j = jsonFromFile()
j.parsingFromFile()
