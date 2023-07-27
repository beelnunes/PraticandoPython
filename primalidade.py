n = int(input("Digite um número inteiro: "))

x = (n - 1)
um = (n == 1)
dois = (n == 2)

while (x > 1):    
    if dois:
        print("primo")
        x = 0
        
    if not((n % x) == 0):
        x = x - 1
    else:
        print("não primo")
        x = 0

if um or x == 1:
    print("primo")
