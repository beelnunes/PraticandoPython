n = int(input("Digite o valor de n: "))

fatorial = n
resultado = 0

while (n > 0) or (n == 0): # so inicia o while para n >= 0
    if (n == 0):            # so roda para n = 0
        fatorial = 1
        print(fatorial)
        n = n - 1           # ponto de parada. Torna o n < 0 e para de rodar o while
    else:
        fatorial = fatorial * (n - 1) # calcula fatorial para n > 0
        n = n - 1                       # mudar o valor de n para continuar a conta
        resultado = (n == 1)
        
    if resultado:           # programa so imprime o resultado quando acabar as multiplicacoes do
        print(fatorial)     # calculo fatorial, ou seja, quando n = 1
        n = n - 2           # torna n < 0 e para de rodar o programa
