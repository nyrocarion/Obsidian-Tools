from ordnung_in_einheitengruppe import order_in_unit

def get_subgroups(n):
    # Check if there a primitive elements that create the group
    primitives = []
    for i in range(1,n):
        if order_in_unit(n,i) == (n-1):
            primitives.append(i)
    if primitives == []:
        print(f"Es handelt sich bei Z_*{n} um keine zyklische Gruppe")
        return None
    else:
        print(f"Die Gruppe Z_*{n} ist zyklisch mit {len(primitives)} Erzeugern")
    print(f"Alle Erzeuger von Z_*{n}: {primitives}")
    # get divisors of n-1 to know how many and what length the subgroups have
    divisors_of_nminusone = []
    for i in range(1,n+1):
        if (n-1) % i == 0:
            divisors_of_nminusone.append(i)
    print(f"Teiler von {n-1}: {divisors_of_nminusone}")
    subgroups = []
    subgroup_primitives = []
    for divisor in divisors_of_nminusone:
        nk = (n-1) // divisor
        primitives_of_subgroup = []
        for x in range(len(primitives)):
            res = primitives[x]**nk % n
            if res not in primitives_of_subgroup:
                primitives_of_subgroup.append(res)
        subgroup_primitives.append(sorted(primitives_of_subgroup))
        # add elements to subgroup
        subgroup = []
        for x in range(0,divisor):
            subgroup.append(res**x % n)
        subgroups.append(subgroup)
    return subgroups,subgroup_primitives

def pretty_print_subgroups(inp):
    subgroups,subgroup_primitives = inp
    # structure row data
    rows = [["Untergruppe", "Elemente", "Primitive Elemente"]]
    for subgroup, primitives in zip(subgroups, subgroup_primitives):
        h_label = f"H_{len(subgroup)}"
        elements = f"{sorted(subgroup)}"
        primitives = f"alpha={primitives}"
        rows.append([h_label, elements, primitives])
    # get max col width for each one
    col_widths = [max(len(row[i]) for row in rows) for i in range(3)]
    headers = "| "+ rows[0][0] + " "*(col_widths[0]-len(rows[0][0])) + " | "
    headers += rows[0][1] + " "*(col_widths[1]-len(rows[0][1])) + " | "
    headers += rows[0][2] + " "*(col_widths[2]-len(rows[0][2])) + " | "
    print(headers)
    dividor = "| "+"-"*col_widths[0]+" | "+"-"*col_widths[1]+" | "+"-"*col_widths[2]+ " |"
    print(dividor)
    for row in rows[1:]:
        h_label = row[0]
        elements = row[1]
        primitives = row[2]
        str = "| " + h_label + " "*(col_widths[0]-len(h_label)) + " | "
        str += elements + " "*(col_widths[1]-len(f"{elements}")) + " | "
        str += primitives + " "*(col_widths[2]-len(f"{primitives}")) + " |"
        print(str)

if __name__ == "__main__":
    n = input("Berechne ob zyklisch und falls gegeben die Untergruppe von Z*_n mit n= ")
    res = get_subgroups(int(n))
    if res != None:
        pretty_print_subgroups(res)
    # | Untergruppe | Elemente                        | Primitive Elemente |
    # | ----------- | ------------------------------- | ------------------ |
    # | H_1         | [1]                             | alpha=[1]          |
    # | H_2         | [1, 10]                         | alpha=[10]         |
    # | H_5         | [1, 3, 4, 5, 9]                 | alpha=[3, 4, 5, 9] |
    # | H_10        | [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | alpha=[2, 6, 7, 8] |
    