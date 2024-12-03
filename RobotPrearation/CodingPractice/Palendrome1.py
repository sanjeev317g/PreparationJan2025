# 12321 on reverse it should still remain same
def palindrome():
    num = 12321
    reverse = 0
    temp = num
    for n in range(len(str(num))):
        rem = num % 10
        reverse = (reverse * 10) + rem
        num = int(num / 10)
    
    if(reverse == temp):
        print("its palindrome")

palindrome()