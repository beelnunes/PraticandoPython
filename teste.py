valor = 50
intervalo = range(0)

while not (valor in intervalo):
  x = 0
  y = x + 25
  intervalo = range(x, y+1)

print(intervalo)
