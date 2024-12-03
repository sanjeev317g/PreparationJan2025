def Anagram():
    ana1 = "silent"
    ana2 = "listen"

    ana11 = {}
    ana22 = {}

    for n_char in ana1:
        if n_char in ana11:
            ana11[n_char] =+ 1
        else:
            ana11[n_char] = 1
    
    for n_char in ana2:
        if n_char in ana22:
            ana22[n_char] =+ 1
        else:
            ana22[n_char] = 1

    if (ana11 == ana22):
        print("its an Anagram")
    else:
        print("Not an Anagram")


Anagram()
