def eprimo(n):
    
    menores_primos = [2,3,5,7] # criterio 1: estar nessa lista
    if n in menores_primos:
        return n
    else:
        for i in menores_primos: # criterio 2: ser multiplo dos menores primos
            nprimo = n % i
            if nprimo == 0:
                return "nao primo"
        
            
    for divisor in range(2,n-1): # criterio 3: ter o resto diferente de 0 e quociente menor que o divisor
        resto = n % divisor
        quociente = n / divisor
            
        if (resto == 0):
            return "nao primo"
        else:
            if (quociente < divisor):
                return n


def maior_primo(m):
    if (m >= 2):
        x = 2
        y = 0
        while x <= (m):
            y = eprimo(x)
            if y != "nao primo":
                z = y

            x = x + 1

    return z


print(maior_primo(101))
