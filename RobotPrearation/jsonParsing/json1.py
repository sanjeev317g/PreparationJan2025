import json

class json1:
    def parseJson(self):
        with open('RobotPrearation\\jsonParsing\\test.json','r') as file:
            data = json.load(file)
            print(data['address']['street'])
j = json1()
j.parseJson()

# import json

# def readjson():
#     with open('.json','r') as file:
#         data = json.load(file)
#         data['address']['stree']

# def readJosn():
#     with open('.json','r') as file:
#         data = json.load(file)
#         data['address']['street']

def isss():
    a= 10
    b = 10
    c = 10
    print(a == b)
    print(a is c)

isss()
