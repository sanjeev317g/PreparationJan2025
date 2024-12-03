def findMissingNumberArray():
    l_list = [1,2,3,4,5,7,8,9]
    s_sum = sum(l_list)
    n= len(l_list) + 1
    e_sum = n * (n+1) // 2
    print(s_sum - e_sum)
findMissingNumberArray()