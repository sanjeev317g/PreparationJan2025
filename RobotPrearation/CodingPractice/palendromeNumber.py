def palendromeNumber():
    number = 121
    # reminder = 0
    reverse = 0
    temp = number
    while(number > 0):

        reminder = number % 10 
        reverse = (reverse * 10) + reminder
        number = int(number / 10)
    if(temp == reverse):
        print(f"{reverse} number is a palendrome")

palendromeNumber()
