def order_in_unit(n,a):
    # Z_n
    # a^i
    n = int(n)
    a = int(a)
    unit = [elem for elem in range(1,11)]
    res = 0
    print(f"|$i$|${a}^i \mod {n}$|")
    print("|-|-|")
    counter = 1
    while res != 1 and counter <= len(unit):
        res = a**counter % n
        print(f"|${counter}$|${a}^{counter}\\equiv{res}\\mod {n}$|")
        counter += 1
    print("-> d.h. $\\text{ord}("+str(a)+")="+str(counter-1)+"$ in $\\mathbb Z_{"+str(n)+"}^*$")

if __name__ == "__main__":
    n = input("Z_n^* with n=           ")
    a = input("Berechne Ordnung von a= ")
    order_in_unit(n,a)
