import json


class parseNestedData:
    def parseData(self):
        with open('RobotPrearation\\jsonParsing\\test1.json','r') as file:
            data = json.load(file)
            print(data["name"])
            print(data["contact"]["email"])
            print(data["contact"]["address"]["city"])
            
            for skill in data["skills"]:
                print(skill["name"], " -", skill["experience"])
            
            for project in data["projects"]:
                print(project["title"], ",")

            print(f"Zip Code - ",{data["contact"]["address"]["zipcode"]})
            
p = parseNestedData()
p.parseData()