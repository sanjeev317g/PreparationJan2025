def largestElement():
    l_list = [1,2,8,3,4,5,6,7]
    tempp = 0
    for n in range(len(l_list)):
        if tempp < l_list[n]:
            tempp = l_list[n]
    print(tempp)

# largestElement()
def largestElement():
    l_list = [1,2,8,3,4,5,6,7]
    temp = 0
    for n in range(len(l_list)):
        if(temp < l_list[n]):
            temp = l_list[n]
    print(temp)
largestElement()

  