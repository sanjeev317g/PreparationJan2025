def FibanacciSerice():
    # 1,2,3,5,8
    n1 = 0
    n2 = 1
    n3 = 0
    for n in range(0,10):
        n3 = n1+n2
        print(n1)
        n1 = n2 
        n2 = n3
FibanacciSerice()