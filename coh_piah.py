import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    diferencas = []
    for i in range(len(as_a)):
        item = as_a[i] - as_b[i]
        diferencas.append(item)

    valores_absolutos = []
    for item in diferencas:
        modulo = abs(item)
        valores_absolutos.append(modulo)
        
    soma = sum(valores_absolutos)

    similaridade = soma / 6

    return similaridade
        
    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = frases_soltas(sentencas)
    palavras = palavras_soltas(frases)

    quantidade_sentencas = len(sentencas)
    quantidade_frases = len(frases)
    quantidade_palavras = len(palavras)
    quantidade_caracteres_sentencas = conta_caracteres(sentencas)
    quantidade_caracteres_frases =  conta_caracteres(frases)
    quantidade_caracteres_palavras = conta_caracteres(palavras)

    wal = quantidade_caracteres_palavras / quantidade_palavras
    ttr = n_palavras_diferentes(palavras) / quantidade_palavras
    hrl = n_palavras_unicas(palavras) / quantidade_palavras
    sal = quantidade_caracteres_sentencas / quantidade_sentencas
    pal = quantidade_caracteres_frases / quantidade_frases
    sac = quantidade_frases / quantidade_sentencas

    return [wal,ttr,hrl,sal,sac,pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    for i in range(len(textos)):
        assinatura_texto = calcula_assinatura(textos[i])
        similaridades.append(compara_assinatura(assinatura_texto,ass_cp))

    menor_valor = min(similaridades)
    indice_texto = similaridades[0:].index(menor_valor)
        
    return indice_texto + 1

#######
def frases_soltas(lista_sentencas):
    '''Recebe uma lista de sentencas e devolve uma lista de frases'''
    lista_frases = []
    for sentenca in lista_sentencas:
        lista_frases.append(separa_frases(sentenca))

    frases_soltas = []
    i = 0
    while i < len(lista_frases):
        for j in range(len(lista_frases[i])):
            item = lista_frases[i][j]
            frases_soltas.append(item)
        i += 1

    return frases_soltas

def palavras_soltas(frases_soltas):
    '''Recebe uma lista de frases e devolve uma lista de palavras'''
    lista_palavras = []
    for frase in frases_soltas:
        lista_palavras.append(separa_palavras(frase))

    i = 0
    b = 0
    palavras_soltas = []
    while i < len(lista_palavras):
        for b in range(len(lista_palavras[i])):
            item = lista_palavras[i][b]
            palavras_soltas.append(item)
        i += 1
    return palavras_soltas

def conta_caracteres(lista):
    n_caracteres = 0
    for i in range(len(lista)):
        n_caracteres_anterior = n_caracteres
        n_caracteres = len(lista[i])
        n_caracteres = n_caracteres_anterior + n_caracteres
    return n_caracteres

#####
assinatura_copia = le_assinatura()

lista_textos = le_textos()

resultado = avalia_textos(lista_textos,assinatura_copia)

print("O autor do texto", resultado, "está infectado com COH-PIAH")


