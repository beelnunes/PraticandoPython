def fatorial(n):
    fatorial = n
    for i in range(n-1):
        fatorial = fatorial * (n - 1)
        n = n - 1
        
    return(fatorial)

def fatorial2(n):
  """Calcula fatorial com o laço while"""
  fat = 1
  if n >= 0:
    while(n > 1):
      fat = fat * n
      n = n - 1
  else:
    fat = ("Não existe fatorial para número negativo")

  return fat


def coeficienteBinomial(n, k):
    coeficienteBinomial = fatorial2(n) / (fatorial2(k) * fatorial2(n - k))

    return coeficienteBinomial

resultado = coeficienteBinomial(10,2)
print(resultado)

def testa_fatorial():
  if fatorial(1) == 1:
    print("Funciona para 1")
  else:
    print("Não funciona para 1")
  if fatorial(0) == 1:
    print("Funciona para 0")
  else:
    print("Não funciona para 0")
  if fatorial(2) == 2:
    print("Funciona para 2")
  else:
    print("Não funciona para 2")
  if fatorial(5) == 120:
    print("Funciona para 5")
  else:
    print("Não funciona para 5")

testa_fatorial()
