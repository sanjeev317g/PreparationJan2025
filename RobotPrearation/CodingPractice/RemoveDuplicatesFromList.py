def removeDuplicate():
    l_list = [10,20,30,40,20,60,10]
    rem_dup = []
    for num in l_list:
        if num not in rem_dup:
            rem_dup.append(num)
    print(rem_dup)
# removeDuplicate()

def removeDuplicates():
    arr = [1,2,3,4,5,1,2,3,4,5]
    l_list = []

    for n in arr:
        if n not in l_list:
            l_list.append(n)
    print(l_list)
removeDuplicates()

