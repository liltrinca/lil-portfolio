def potencia(x, k):
  parcial = 1
  for i in range(0, k):
    parcial = parcial*x
  return parcial

def pg(x, eps):
  atual = x
  prox = x/2
  soma = atual
  while(atual - prox >= eps):
    soma = soma + prox
    atual = prox
    prox = prox * (x/2)
  return soma

def ocorre(t, p, posicao):
  if t[posicao]==p:
    return True
  return False

def conta_ocorrencia(t,p):
  ocorrencias = 0
  for i in range(0, len(t)):
    if(ocorre(t,p,i)):
      ocorrencias = ocorrencias+1
  return ocorrencias