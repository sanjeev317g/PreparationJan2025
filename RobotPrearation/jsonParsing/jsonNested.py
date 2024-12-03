import json

class nestedJsonParsing:
    def parsingNestedJson(self):
        with open('RobotPrearation\\jsonParsing\\test1.json','r') as file:
            data = json.load(file)
            print(data['contact']['address']['zipcode'])
p = nestedJsonParsing()
p.parsingNestedJson()
            