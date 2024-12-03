import json

class ParsingJsonFile:

    def parsingJsonFile(self):
        with open('RobotPrearation\\jsonParsing\\test.json', 'r') as file:
            data = json.load(file)
            print(f'first name -', {data['firstName']})
            print(data['courses'][2])
            print(data['address']['city'])
p = ParsingJsonFile()
p.parsingJsonFile()