n = int(input("Digite um valor inteiro: "))

expoente = 100
resto = n
igual = 0
soma = 0
metade = 0

while (expoente > -1):
    
    if (n // 10) == 0:
        print("nao")
        expoente = -1
    else:
        digito1 = resto // 10**expoente
        resto = resto % 10**expoente
        expoente = expoente - 1    
        digito2 = resto // 10**expoente
   
        igual = (digito1 == digito2)
        soma = digito1 + digito2
        metade = soma // 2
            
        if igual and (metade == digito1) and (n != resto):
            print("sim")
            expoente = -2

        if expoente == 0:
            print("nao")
            expoente = -1
        

