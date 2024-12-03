

    
def prime():
        for n in range(2, 20):
            if(primeNumbers(n)):
                  print(f"{n} is a prime number")


def primeNumbers(n):
        for i in range(2, n):
            if(n % i == 0):
                return False
        return True
prime()
    

