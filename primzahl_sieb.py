def f(x,m,n):
    return (x + int(m))**2 -int(n) 

def sieb_latex(n=11111,m=105,b=15,c=10):
    table = ""
    # # TODO Prim-Listen erstellen
    p = [2,3,5,7,9,11,13,17,19,23,29]
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
            print("no case",table)
            continue # goes back to loop head
        for fs in funktionswerte:
            add = "-|"
            if (funktionswerte.index(fs)-int(c))%sieb_prim in teilbar:
                while fs % sieb_prim == 0:
                    add = "$"+str(int(fs / sieb_prim))+"$|"
                    fs = fs / sieb_prim
            else:
                print("kein vielfaches der teiler bei ",(funktionswerte.index(fs)-int(c)))
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
