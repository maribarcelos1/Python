def numeroprimo(numero):
  if numero<=1:
    return False
  for n in range(2,numero-1):
    if numero % n == 0:
      return False
  return True

n = int(input("Digite um número:"))
print(numeroprimo(n))
