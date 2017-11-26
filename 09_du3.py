def vytvoreni_slovniku():
    n=int(input("Zadej cislo: "))
    slovnik=dict()
    for cislo in range(1,n+1):
        slovnik[cislo]=cislo**2
    print(slovnik)
    return(slovnik)

def print_the_key_value_pair():
    slovnik=vytvoreni_slovniku()
    for klic in slovnik:
        print(klic, slovnik[klic])
print_the_key_value_pair()     
