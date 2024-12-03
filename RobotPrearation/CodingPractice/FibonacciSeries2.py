# 1,1,2,3,5,6
def fibanacciSeries():
    num1 = 0 
    num2 = 1
    num3 = 0
    for n in range(10):
        num3 = num1+ num2
        print(num1)
        num1 = num2
        num2 = num3

fibanacciSeries()

