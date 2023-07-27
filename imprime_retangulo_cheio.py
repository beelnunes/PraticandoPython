largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))


while altura > 0:
    for i in range(largura):
        print("#", end = "")
    print()
    altura = altura - 1
    
