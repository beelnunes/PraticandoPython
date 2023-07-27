# Escreva a função remove_repetidos que recebe como parâmetro
# uma lista com números inteiros, verifica se tal lista possui
# elementos repetidos e os remove. A função deve devolver uma lista
# correspondente à primeira lista, sem elementos repetidos. A lista
# devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?


def remove_repetidos(lista):
    lista.sort()
    i = 0
    j = 1
    y = 1
    k = 2
    while i < len(lista) - 1:
        
        a = lista[i]
        b = lista[j]
        if a == b:
            del lista[i]
        i = i + 1
        j = i + 1
        for y in range(len(lista)-1):
            c = lista[y]
            d = lista[k]
            if c == d:
                del lista[y]
            k = y + 1
        
    return lista

lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))

