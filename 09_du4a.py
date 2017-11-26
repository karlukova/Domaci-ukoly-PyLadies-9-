import random
seznam_odpovedi= list()
for i in (0,6):
    sada_odpovedi=dict()
    kdo_odpoved=input('Kdo?')
    s_kym_odpoved=input('S kym?')
    co_delali_odpoved=input('Co delali?')
    kde_odpoved=input('Kde? ')
    kdy_odpoved=input('Kdy? ')
    proc_odpoved=input('Proc? ')
    sada_odpovedi={'kdo':kdo_odpoved, 's_kym':s_kym_odpoved, 'co_delali':co_delali_odpoved, 'kdy':kdy_odpoved, 'kde':kde_odpoved, 'proc':proc_odpoved}
    seznam_odpovedi.append(sada_odpovedi)
veta=list()
for k in (0, 6): 
    sada_odpovedi=seznam_odpovedi[k] #does not work, don't know how to access a dictionary in the list while using a loop
    slovo= sada_odpovedi[random.choice(list(sada_odpovedi.keys()))]
    veta.append(slovo)
print(veta)
