def AnagramCheck():
    ana1 = "listen"
    ana2 = "silent"

    ana11 = {}
    for char in ana1:
        if char in ana11:
            ana11[char] += 1
        else:
            ana11[char] = 1

    ana22 = {}
    for char in ana2:
        if char in ana22:
            ana22[char] =+ 1
        else:
            ana22[char] = 1

    print(ana11)
    print(ana22)

AnagramCheck()


