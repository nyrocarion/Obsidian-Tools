def f(x,m,n):
    return (x + int(m))**2 -int(n) 

def sieb_latex(n=11111,m=105,b=15,c=10):
    table = ""
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009]
    menge_prim_b = [prim for prim in p if prim <= int(b)]
    sieb_intervall_c = [x for x in range(-int(c),int(c)+1)]
    funktionswerte = []
    # S-Werte
    table += "|$s$|"
    for s in sieb_intervall_c:
        table += "$"+str(s)+"$|"
    print(table)
    # Hline
    table = "|"
    for s in range(len(sieb_intervall_c)+1):
        table += "-|"
    print(table)
    # Funktionswerte
    table = "|$f(s)$|"
    for s in sieb_intervall_c:
        table += "$"+str(f(s,m,n))+"$|"
        funktionswerte.append(f(s,m,n))
    print(table)
    # Sieb mit XY
    for sieb_prim in menge_prim_b:
        table = "|Sieb mit $"+str(sieb_prim)+"$|"
        # Test für die ersten p Elemente aus s um nicht Vielfache auszuschließen
        start_initial = int(c)
        end_initial = int(c)+sieb_prim
        if end_initial >= len(funktionswerte):
            end_initial = len(funktionswerte)-1
        initial_list = funktionswerte[start_initial:end_initial]
        teilbar = []
        for s in initial_list:
            if s % sieb_prim == 0:
                teilbar.append(initial_list.index(s))
        if teilbar == []:
            table += "|"
            for fs in funktionswerte:
                table += "-|"
            print(table)
            continue # goes back to loop head
        for fs in funktionswerte:
            add = "-|"
            if (funktionswerte.index(fs)-int(c))%sieb_prim in teilbar:
                while fs % sieb_prim == 0:
                    add = "$"+str(int(fs / sieb_prim))+"$|"
                    fs = fs / sieb_prim
            table += add
        print(table)
            
if __name__ == "__main__":
    print("Bitte Parameter eingeben!")
    print("Der Algorithmus ist noch bruteforce basiert und unschön")
    n = input("Die Zahl n")
    m = int(int(n)**0.5)
    b = input("Schranke der Primzahlen (B) (max 1000)")
    c = input("Schranke des Siebintervalls(-+C)")
    sieb_latex(n,m,b,c)
