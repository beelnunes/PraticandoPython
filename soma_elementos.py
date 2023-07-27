def soma_elementos(lista):
    n = 0
    for i in range(len(lista)):
        n = lista[i] + n

    return n


lista = [2, 4, 2, 2, 3, 3, 1]
print(soma_elementos(lista))
