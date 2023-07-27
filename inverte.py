lista = []
listaInversa = []
indice = -1
indiceNegativo = 0

n = int(input("Digite um numero? "))

while n != 0:
    lista.append(n)
    n = int(input("Digite um numero? "))

for i in range(len(lista)):
    listaInversa.append(0)

for i in range(len(lista)):
    indiceNegativo = indiceNegativo - 1
    print(lista[indiceNegativo])




