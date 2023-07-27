def main():
    """
    Devolve os coeficientes da expansão de
    (x + y) elevado a e.
    """
    e = int(input("Digite o valor do expoente: "))
    k = 0
    coeficientesExpansao = []
    for k in range(e + 1):
        coeficienteNovo = coeficienteBinomial(e, k)
        coeficientesExpansao.append(coeficienteNovo)
        k =+ 1 # mesmo que k = k + 1

    return coeficientesExpansao

def fatorial(n):
  """Calcula fatorial com o laço while"""
  fat = 1
  if n >= 0:
    while(n > 1):
      fat = fat * n
      n = n - 1
  else:
    fat = ("Não existe fatorial para número negativo")

  return fat



def coeficienteBinomial(n , k):
    """
    Calcula a combinação de n elementos de
    organizados em grupos de k em k.
    """
    coeficienteBinomial = fatorial(n) / (fatorial(k) * fatorial(n - k))

    return coeficienteBinomial
