def primeNumber(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def p_Number():
    for n in range(2, 20):
        if(primeNumber(n)):
            print(f"{n} is a prime number")