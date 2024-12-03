def p_Number():
    for n in range(2, 20):
        if(PrimeNumber(n)):
            print(f"{n} is Prime")


def PrimeNumber(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True  

p_Number()  
    