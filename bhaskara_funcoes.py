from __future__ import print_function
from cgi import print_arguments
import math
from os import sep

def delta(a,b,c):
    return b **2 - 4*(a)*(c)


def raizEquacao2g(a,b,c):
    
    valorDelta = delta(a,b,c)
    
    if (valorDelta > 0):
        
        raiz1 = (-b + math.sqrt(valorDelta)) / (2 * a)
        raiz2 = (-b - math.sqrt(valorDelta)) / (2 * a)
        return [raiz1, raiz2]
        
    else:
        
        if (valorDelta < 0):
            return ("esta equacao nao possui raizes reais")
            
        else:
            
            raiz = (-b + math.sqrt(valorDelta)) / (2 * a)
            print("a raiz dupla desta equacao e",raiz)
            return raiz


raiz1 = raizEquacao2g(-2,5,10)
raiz2 = raizEquacao2g(1,1,1)
raiz3 = raizEquacao2g(-2,-5,-10)

print(raiz1)
print(raiz2)
print(raiz3)

