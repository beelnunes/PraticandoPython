largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))

parteVazada = largura - 2
miolo = altura - 2


for i in range(largura):
    print("#", end = "")
print()
    
while miolo > 0:
    print("#", end = "")
    for i in range(parteVazada):
        print(" ", end = "")
    print("#")
    miolo = miolo - 1

for i in range(largura):
    print("#", end = "")
print()
