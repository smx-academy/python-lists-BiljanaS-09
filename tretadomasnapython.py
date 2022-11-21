#prva zadaca
"""
lista = []
zbir = 0

for i in range(10):
    broj = int (input("Vnesete broj: "))
    lista.append(broj)
    
zbir = sum(lista)   
print(lista)    
print("Zbirot na elementite od listot iznesuva: ", zbir)
"""
#vtora zadaca
"""
lista1 = []

n = int (input("Vnesete kolku elementi ke ima listata: "))

for i in range(n):
    broj = int (input("Vnesete broj: "))
    lista1.append(broj)
    max_el=max(lista1)

print("Max element vo listata e: ",max_el)
"""
#treta zadaca
"""
lista2 = []
n = int (input("Vnesete kolku elementi ke ima listata: "))

for i in range(n):
    x = input("Vnesete element: ")
    lista2.append(x)
print(lista2)

y = input("Dali sakate da izbrisete nekoj el od listata: da/ne ")

if y == "da":
    z = int (input("Kolku elementi ke izbrisete? "))
    
    for k in range(z):
        d = int (input("Koj element ke go izbrisete "))
        del lista2[d]

print(lista2)
"""
#cetvrta zadaca
"""
lista3 = []

n = int (input("Vnesete kolku iminja ke ima listata: "))

for i in range(n):
    x = input("Vnesete ime: ")
    lista3.append(x)
    max_ime = max(lista3, key=len)
    
print(lista3)
print("Vo listata najdolgo ime e  ",max_ime)
"""
#petta zadaca
"""
lista4 = []

n = int (input("Vnesete kolku elementi ke ima listata: "))

for i in range(n):
    broj = int (input("Vnesete broj: "))
    lista4.append(broj)
    max_el=max(lista4)

print(lista4)
lista4.remove(max_el)

max_el_nov=max(lista4)
print("Vtor max element vo listata e: ",max_el_nov)
"""
#sesta zadaca
produkti = []
ceni = []

while True:
    produkt = input("Vnesete produkt: ")
    cena = int (input("Vnesete cena za produktot: "))
    produkti.append(produkt)
    ceni.append(cena)
    answer=input("Dali sakate da platite? da/ne ")
    if answer.lower() == "ne":
        pass 
    else:
        vkupno=sum(ceni)
        break

print(produkti)
print(ceni)  
print("Treba da platite {} denari vkupno: ".format(vkupno))
       
k = int(input("Vnesete kolku pari ke platite: "))
kusur = k-vkupno
if kusur>0:
    print("Vasiot kusur e: {} denari".format(kusur))
elif kusur == 0:
    print("Nemate kusur za vrakanje")
else:
    print("Treba da doplatite uste {} denari".format(-kusur))
   
    
      
