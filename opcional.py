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


def n_primos():
    numero = int(input("Digite um numero maior ou igual a 2: "))

    quantidade = 0

    for i in range(2,numero):
        if eprimo(i) == True:
            quantidade += 1

    return quantidade
