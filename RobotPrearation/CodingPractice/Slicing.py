# reversing a string 
def reverse_String():
    string = "Carrier Automation"
    print(string[::-1])
# reverse_String()

def GetSubstring():
    string = "Carrier Automation"
    print(string[7:15])
# GetSubstring()

def ExtractEverySecondCharacter():
    string = "Carrier Automation"
    print(string[::2])
# ExtractEverySecondCharacter()

def extractLastThreeCharOfString():
    string = "Carrier Automation"
    print(string[-3:])
# extractLastThreeCharOfString()

def extractFirstAndLastCharOfString():
    string = "Carrier Automation"
    print(string[1:-1])
# extractFirstAndLastCharOfString()

def stepSize_Slicing():
    s = "abcdef"
    step = s[::2]  # Every second character
    print(step)  # Output: ace
# stepSize_Slicing()

def extractFirstFourElementFromList():
    lists = [10, 20, 30, 40, 50, 60]
    print(lists[:4])
# extractFirstFourElementFromList()

def lastElementFromList():
    lists = [10, 20, 30, 40, 50, 60] 
    print(lists[-1:])
# lastElementFromList()

def reversingList():
    lists = [10, 20, 30, 40, 50, 60]
    print(lists[::-1])
reversingList()


