def eprimo(n):
    
    menores_primos = [2,3,5,7] # criterio 1: estar nessa lista
    if n in menores_primos:
        return True
    else:
        for i in menores_primos: # criterio 2: ser multiplo dos menores primos
            nprimo = n % i
            if nprimo == 0:
                return False
        
            
    for divisor in range(2,n-1): # criterio 3: ter o resto diferente de 0 e quociente menor que o divisor
        resto = n % divisor
        quociente = n / divisor
            
        if (resto == 0):
            return False
        else:
            if (quociente < divisor):
                return True

#####
            
numero = int(input("Digite um numero inteiro >1: "))

fator = 2
multiplicidade = 0

while numero > 1:
    while eprimo(fator):
        while numero % fator == 0:
            multiplicidade = multiplicidade + 1
            numero = numero / fator
        if multiplicidade > 0:
            print("Fator:", fator,"Multiplicidade:", multiplicidade, sep = "\t")
            multiplicidade = 0
        fator = fator + 1
    fator = fator + 1
        
