import math
def f(x,m,n):
    return (x + int(m))**2 -int(n) 

def sieb_latex(n=11111,m=105,b=15,c=10):
    table = ""
    # Listen erstellen
    p = [2,3,5,7,9,11,13,17,19,23,29]
    menge_prim_b = []
    for prim in p:
        if prim <= int(b):
            menge_prim_b.append(prim)
    sieb_intervall_c = []
    c = int(c)
    start = -c
    end = c+1
    for x in range(start,end):
        sieb_intervall_c.append(x)
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
        for fs in funktionswerte:
            add = "-|"
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
    b = input("Schranke der Primzahlen (B) gerade nur bis 29 max")
    c = input("Schranke des Siebintervalls(-+C)")
    sieb_latex(n,m,b,c)
