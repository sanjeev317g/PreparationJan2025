def Palendrome():
    number = 12321
    temp = number
    reverse = 0
    for n in range(5):
        data = number % 10 
        reverse = (reverse*10) + data
        number = int(number /10)
    if(temp == reverse):
        print(f"{reverse} is a palendrome")

Palendrome()

