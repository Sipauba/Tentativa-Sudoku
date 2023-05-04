import random
lista = []
numero = random.randint(1, 9)
lista.append(numero)
print(lista)
x = 0
contador = 0
incluiu = True
gerador = True
while x < 9:
    contador = contador + 1
    if incluiu == True:
        x = x + 1
        contador = 0
        incluiu = False
    if contador >= x:
        contador = 0
    #if contador != 0:
    if gerador == True or achou == True:
        numero = random.randint(1, 9)
        contador = 0
        gerador = False


    print(numero)
    print("x", x)

    print("contador",contador)
    achou = False
    while contador < x:
        if lista[contador] == numero:
            #contador = contador + 1
            achou = True
            break
        elif achou == False and contador == x - 1:
            lista.append(numero)
            incluiu = True
            gerador = True
            #x = x + 1
            break
        else:
            break
print(lista)
lista2 = lista.copy()
lista3 = lista.copy()
lista4 = lista.copy()
lista5 = lista.copy()
lista6 = lista.copy()
lista7 = lista.copy()
lista8 = lista.copy()
lista9 = lista.copy()

chave = False
while chave == False:
    random.shuffle(lista)
    random.shuffle(lista2)
    random.shuffle(lista3)
    random.shuffle(lista4)
    random.shuffle(lista5)
    random.shuffle(lista6)
    random.shuffle(lista7)
    random.shuffle(lista8)
    random.shuffle(lista9)
    if lista != lista2 != lista3 != lista4 != lista5 != lista6 != lista7 != lista8 != lista9:
        chave =True

print()
print(lista)
print(lista2)
print(lista3)
print(lista4)
print(lista5)
print(lista6)
print(lista7)
print(lista8)
print(lista9)