def vytvoreni_slovniku():
    n=int(input("Zadej cislo: "))
    slovnik=dict()
    for cislo in range(1,n+1):
        slovnik[cislo]=cislo**2
    print(slovnik)
    return(slovnik)

def suma_klicu_a_hodnot():
    slovnik1=vytvoreni_slovniku()
    suma_hodnot=sum(slovnik1.values())
    print(suma_hodnot)
    suma_klicu=sum(slovnik1)
    print(suma_klicu)

suma_klicu_a_hodnot()
