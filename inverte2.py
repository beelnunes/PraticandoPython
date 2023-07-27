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
    indice = indice + 1
    indiceNegativo = indiceNegativo - 1
    listaInversa[indiceNegativo] = lista[indice]

print(lista)    
print(listaInversa)



