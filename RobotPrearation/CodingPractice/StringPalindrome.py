def string_palindrome():
    str1 = "racecar"
    str2 = str1[::-1]
    print(str2)
    if(str2 == str1):
        print("String is palindrome")
    else:
        print("Not a palindrome")

string_palindrome()