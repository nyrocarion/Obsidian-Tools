from math import sqrt, floor

def probedivision(n:int,silent=False):
    '''
    @param: n int
        an uneven number which is tested for divisors
    This Function tests if the number n can be divided by anything
    else than 1 and n itself
    If that is the case it isnt a prime
    '''
    limit = floor( sqrt(n) )
    candidates = [x for x in range(3,n) if x % 2 == 1]
    for candidate in candidates:
        if n % candidate == 0: # if an uneven number divides
            if not silent:
                print(f"n={n} is not a prime! witness against primality: {candidate}")
            return candidate
    if not silent:
        print(f"n={n} is a prime")
    return None

def faktorisieren(n: int, faktoren=[]):
    faktor = probedivision(n,True)
    if faktor == None:
        faktoren.append(n)
        print(f"Factors of n: {sorted(faktoren)}")
        return n
    else:
        faktoren.append(faktor)
        new_n = n // faktor
        faktorisieren(new_n,faktoren)
    

if __name__ == "__main__":
    inp = input("Enter a number that should be tested for divisors. n= ")
    res = probedivision(int(inp))
    faktorisieren(int(inp),[])
