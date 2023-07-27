n = int(input("Digite um valor inteiro: "))

expoente = 100
resto = n
soma = 0


while (expoente > -1):
    
    digito = resto // 10**expoente
    resto = resto % 10**expoente
    expoente = expoente - 1
    soma = soma + digito
    
    if expoente < 0:
        print(soma)

