def dict_from_string():

    retezec=input("Zadej retezec: ")
    seznam=list(retezec)
    retezec.split(',')
    print(seznam)
    slovnik=dict()
    for znak in seznam:
        slovnik.update({znak:seznam.count(znak)})
    print(slovnik)

dict_from_string()
