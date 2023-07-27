x = int(input("Digite um número inteiro:"))

dezena = (((x % 100) - (x % 10)) // 10)

print("O dígito das dezenas é", dezena)
