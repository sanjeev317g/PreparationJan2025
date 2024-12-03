def Lambda():
    # syntax "lambda arguments : expression"
    x = lambda a: a+15
    print(x(5))

    x1 = lambda a, b : a* b
    print(x1(2,2))

    x2 = lambda a : "Even Numbers" if (a % 2 == 0) else "fdsfds"
    print(x2(3))


Lambda()