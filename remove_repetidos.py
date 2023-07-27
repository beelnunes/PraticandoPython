# Escreva a função remove_repetidos que recebe como parâmetro
# uma lista com números inteiros, verifica se tal lista possui
# elementos repetidos e os remove. A função deve devolver uma lista
# correspondente à primeira lista, sem elementos repetidos. A lista
# devolvida deve estar ordenada.

# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?


def remove_repetidos(lista):
    novaLista = []
    lista.sort()

    for i in range(len(lista)):
        if not lista[i] in novaLista:
            novaLista.append(lista[i])
            
    return novaLista

lista = [2, 4, 2, 2, 3, 3, 1]
print(remove_repetidos(lista))

