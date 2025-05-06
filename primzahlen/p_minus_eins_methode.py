import math

def transform_int_to_bin(input: int) -> list[int]:
    output = ""
    while input > 0:
        output = str(input & 1) + output
        input >>= 1
    return [int(num) for num in output]

def square_and_multiply_wo_mod(a, k):
    # a^k \mod N
    k_bin = transform_int_to_bin(k)
    k_bin.reverse()
    l = len(k_bin) - 1  
    x = dict()
    x[l] = a 
    
    i = l
    while i > 0:
        y = (x[i] ** 2) 
        i -= 1
        if k_bin[i] == 0:
            x[i] = y 
        else:
            x[i] = (y * a) 
    return x[0]

def prime(upto):
    # Code from https://rebrained.com/?p=458
    primes=[2]
    for num in range(3,upto+1,2):
        isprime=True
        for factor in range(3,1+int(math.sqrt(num)),2):
             if not num % factor: isprime=False; break
        if isprime: primes.append(num)
    return primes

def pminusone(n,b):
    p = prime(1000)
    # K berechnen
    k = 1
    for prim in p:
        if prim <= b:
            exp = 1
            while prim**exp <= b:
                exp += 1
            exp -= 1
            k = k * (prim**exp)
        else:
            break
    # Echten Teiler überprüfen
    gcd = math.gcd(square_and_multiply_wo_mod(2,k)-1,n)
    if gcd != 1:
        print(f"Echter Teiler von {n}: {gcd}")
        print(f"Gefunden bei b={b} mit k={k}")
        return gcd
    return False

def repeat_pminusone(n):
    # B-Werte durchprobieren
    n = int(n)
    limit = 1000
    for b in prime(limit):
        gcd = pminusone(n,b)
        if gcd > 0: # nicht der False Fall
            return str(gcd) +"*"+str(int(n/gcd))


if __name__ == "__main__":
    print("Faktorisierungsalgorithmus für große zusammengesetzte Zahlen basierend auf der p-1-Methode")
    print("Läuft eher langsam weil ich nicht auf Performance geachtet habe\n")
    print("Bitte Parameter eingeben!")
    n = input("Die Zahl n von der ein echter Teiler bestimmt werden soll: ")
    faktoren_n = repeat_pminusone(n)
    print(f"{n}={faktoren_n}")

