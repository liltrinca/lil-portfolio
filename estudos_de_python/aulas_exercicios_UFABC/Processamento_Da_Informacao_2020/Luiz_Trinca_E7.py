def exercicio1(A: list) -> int:
  a = list(set(A))
  nrep = 0
  nrepant = 0
  for i in a:
    moda = 0
    nrep = A.count(i)
    nrepant = nrep
    if (nrep > nrepant):
      moda = A[A.index(i)]
  return moda, nrep

def exercicio2(A:list) -> list:
  pivo, B = A[0], []
  for i in range(len(A)):
    if (A[i] <= pivo):
      B.append(A[i])
  maxi = len(B)-1
  B[0] = B[maxi]
  B[maxi] = pivo
  for j in range(len(A)):
    if (A[j] > pivo):
      B.append(A[j])
  return B

def exercicio5(n: int) -> list:
  for x in range(1,n+1):
    for y in range(1,n+1):
      for z in range(1,n+1):
        if(x != y and x != z and y != x and y != z and z != x and z != y):
          print([x,y,z])

def exercicio6(n:int, k:int) -> tuple:
  tupla = ()
  for i in range(1,n):
    for j in range(1,n):
      tupla = (i,j+1)
      if(tupla[1] > tupla[0]):
        print(tupla)