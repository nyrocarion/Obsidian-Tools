import math

def transform_int_to_bin(input: int) -> list[int]:
    output = ""
    while input > 0:
        output = str(input & 1) + output
        input >>= 1
    return [int(num) for num in output]

def square_and_multiply(a, k, N):
    # a^k \mod N
    k_bin = transform_int_to_bin(k)
    k_bin.reverse()
    l = len(k_bin) - 1  
    x = dict()
    x[l] = a % N  
    
    i = l
    #print(f"Step i = {i} with b_{i} = {k_bin[i]:1}")
    #print(f"x_{i} = a = {x[i]}\n")
    while i > 0:
        y = (x[i] ** 2) % N
        i -= 1
        if k_bin[i] == 0:
            x[i] = y 
        else:
            x[i] = (y * a) % N
        #print(f"Step i = {i} with b_{i} = {k_bin[i]:1}")
        #print(f"y = x_{i+1}^2 = {x[i+1]}^2 = {y} mod {N}")
        if k_bin[i] == 0:
            #print(f"x_{i} = y = {y} mod {N}\n")
            pass
        else:
            #print(f"x_{i} = y * a = {y} * {a} = {x[i]} mod {N}\n")
            pass
    return x[0]

def square_and_multiply_wo_mod(a, k):
    # a^k \mod N
    k_bin = transform_int_to_bin(k)
    k_bin.reverse()
    l = len(k_bin) - 1  
    x = dict()
    x[l] = a 
    
    i = l
    #print(f"Step i = {i} with b_{i} = {k_bin[i]:1}")
    #print(f"x_{i} = a = {x[i]}\n")
    while i > 0:
        y = (x[i] ** 2) 
        i -= 1
        if k_bin[i] == 0:
            x[i] = y 
        else:
            x[i] = (y * a) 
        #print(f"Step i = {i} with b_{i} = {k_bin[i]:1}")
        #print(f"y = x_{i+1}^2 = {x[i+1]}^2 = {y} mod {N}")
        if k_bin[i] == 0:
            #print(f"x_{i} = y = {y} mod {N}\n")
            pass
        else:
            #print(f"x_{i} = y * a = {y} * {a} = {x[i]} mod {N}\n")
            pass
    return x[0]

def prime(upto):
    # ty https://rebrained.com/?p=458
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
    print("k für b:",b,":",k)
    gcd = math.gcd(square_and_multiply_wo_mod(2,k)-1,n)
    if gcd != 1:
        print("Echter Teiler:",gcd)
        return True
    return False

for b in prime(100):
    if pminusone(275237,b):
        break
