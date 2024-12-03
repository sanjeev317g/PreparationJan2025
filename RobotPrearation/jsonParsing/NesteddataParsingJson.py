import  json

class NesteddataParsingJson:
    def nestedDataParsing(self):
        with open('RobotPrearation\\jsonParsing\\test1.json', 'r') as file:
            data = json.load(file)
            print('User ID - ',data['id'])
            print('User EMail -', data['contact']['email'])
            print('contact - ', data['contact']['address']['state'])
            print('skills -', data['skills'][0])
            print('skills -', data['skills'][1])
            print('projects -', data['projects'][0])
            print('projects -', data['projects'][1])
    
    def itteratingJsonFile(self):
        with open('RobotPrearation\\jsonParsing\\test1.json', 'r') as file:
            data = json.load(file)
            for skill in data['skills']:
                print(skill['name'], " -", skill['experience'])
            
            for project in data['projects']:
                print(project['title'], "- ", project['role'])
                
                




np = NesteddataParsingJson()
# np.nestedDataParsing()
np.itteratingJsonFile()


