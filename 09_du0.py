def vytvoreni_slovniku():
    n=int(input("Zadej cislo: "))
    slovnik=dict()
    for cislo in range(1,n+1):
        slovnik[cislo]=cislo**2
    print(slovnik)   
vytvoreni_slovniku()
