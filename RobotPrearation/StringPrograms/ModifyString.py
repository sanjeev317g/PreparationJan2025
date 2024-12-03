# String is a immutable cannot change the string.

def Change_String():
    str1 = "Hello aorld"
    l_list = list(str1)
    l_list[6] = 'W'
    str1 = str(l_list)
    print(str1)

Change_String()