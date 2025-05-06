import math
def f(x,m,n):
    return (x + int(m))**2 -int(n) 

def prime(upto):
    # ty https://rebrained.com/?p=458
    primes=[2]
    for num in range(3,upto+1,2):
        isprime=True
        for factor in range(3,1+int(math.sqrt(num)),2):
             if not num % factor: isprime=False; break
        if isprime: primes.append(num)
    return primes

def sieb_latex(n,m,b,c):
    table = ""
    final_output = []
    menge_prim_b = prime(int(b))
    sieb_intervall_c = [x for x in range(-int(c),int(c)+1)]
    funktionswerte = []
    # S-Werte
    table += "|s|"
    for s in sieb_intervall_c:
        table += ""+str(s)+"|"
    print(table)
    final_output.append(table)
    # Funktionswerte
    table = "|f(s)|"
    for s in sieb_intervall_c:
        table += ""+str(f(s,m,n))+"|"
        funktionswerte.append(f(s,m,n))
    print(table)
    final_output.append(table)
    # Sieb mit XY
    for sieb_prim in menge_prim_b:
        table = "|Sieb mit "+str(sieb_prim)+"|"
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
            for fs in funktionswerte:
                table += "-|"
            print(table)
            final_output.append(table)
            continue # goes back to loop head
        for i in range(len(funktionswerte)):
            add = "-|"
            if (i-int(c))%sieb_prim in teilbar:
                while funktionswerte[i] % sieb_prim == 0:
                    add = ""+str(int(funktionswerte[i] / sieb_prim))+"|"
                    funktionswerte[i] = funktionswerte[i] / sieb_prim
            table += add
        print(table)
        final_output.append(table)
    return final_output

def format_markdown_table_console_friendly(lines: list[str], latex: bool = False) -> str:
    ### CHAT GPT CODE
    """
    Formatiert eine Markdown-Tabelle mit optionaler Hervorhebung für -1 und 1.
    Die Kopfzeile (s-Werte) und Trennzeile bleiben farblich unbeeinflusst.

    :param lines: Liste der Zeilen als Strings, jeweils '|' getrennt.
    :param latex: Wenn True, werden Zahlen in $...$ eingefasst und \color verwendet.
    :return: Markdown-kompatibler Tabellenstring.
    """
    # Tabelle als Listen von Zellen parsen
    table = [line.strip('|').split('|') for line in lines]

    # Spaltenanzahl normalisieren
    max_cols = max(len(row) for row in table)
    for row in table:
        while len(row) < max_cols:
            row.append("")
        if len(row) > max_cols:
            row[:] = row[:max_cols]

    # Hilfsfunktion zum Entfernen von ANSI-Farbcodes (sehr einfach, keine externen Module!)
    def strip_ansi(text):
        result = ""
        skip = False
        i = 0
        while i < len(text):
            if text[i] == '\x1b':
                skip = True
            if not skip:
                result += text[i]
            if skip and text[i] == 'm':
                skip = False
            i += 1
        return result

    # Sichtbare Zeichenlänge ohne ANSI-Codes
    def visible_len(s):
        return len(strip_ansi(s))

    # Inhalte einfärben (ab dritter Zeile, nicht bei s-Zeile oder Trennzeile)
    for row_index in range(2, len(table)):
        row = table[row_index]
        for i in range(len(row)):
            val = row[i].strip()
            if val in {"-1", "1"}:
                if latex:
                    table[row_index][i] = f"${{\\color{{green}}{val}}}$"
                else:
                    table[row_index][i] = f"\x1b[32m{val}\x1b[0m"
            elif latex:
                try:
                    float(val)
                    table[row_index][i] = f"${val}$"
                except:
                    pass  # Kein numerischer Wert, nicht ändern

    # Spaltenbreiten berechnen
    col_widths = [0] * max_cols
    for row in table:
        for i in range(max_cols):
            col_widths[i] = max(col_widths[i], visible_len(row[i]))

    # Zeilen formatiert zusammensetzen
    def format_row(row):
        return "|" + "|".join(row[i] + " " * (col_widths[i] - visible_len(row[i])) for i in range(max_cols)) + "|"

    # Markdown-Zeilen zusammensetzen
    result_lines = []
    for i, row in enumerate(table):
        result_lines.append(format_row(row))
        if i == 0:  # Nach der Kopfzeile Trennlinie
            result_lines.append("|" + "|".join("-" * col_widths[i] for i in range(max_cols)) + "|")

    return "\n".join(result_lines)
            
if __name__ == "__main__":
    print("Bitte Parameter eingeben!")
    n = input("Die Zahl n:                                                    ")
    m = int(int(n)**0.5)
    b = input("Schranke der Primzahlen (B):                                   ")
    c = input("Schranke des Siebintervalls(-+C):                              ")
    formatlatex = input("Für Markdown-Latex-Ausgabe bitte True hier eingeben: ")
    output = sieb_latex(n,m,b,c)
    print(format_markdown_table_console_friendly(output,bool(formatlatex)))
    

