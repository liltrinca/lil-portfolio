def exercicio1(A: [[float]]) -> [[float]]:
  nlinha = len(A)
  ncoluna = len(A[0])
  frobe = 0.0
  for i in range(nlinha):
    for j in range(ncoluna):
      frobe += (abs(A[i][j])**2)**(1/2)
  return frobe

def exercicio2(A:list) -> bool:
  transp, iden, C, valor = [], [], [], 0
  for i in range(len(A[0])):
    transp.append([A[j][i] for j in range(len(A))])
  for j in range(len(A)):
    iden.append([])
    for k in range(len(A)):
      if j != k:
        iden[j].append(0)
      else:
        iden[j].append(1)
  for l in range(len(A)):
    C.append([])
    for m in range(len(A)):
      C[l].append(0)
  for a in range(len(A)):
    for b in range(len(A)):
      for m in range(len(A)):
        valor += (A[a][m] * transp[m][b])
      C[a][b] = valor
      valor = 0
  if(C == iden):
    return True
  else: return False

def exercicio3(A: [[float]]) -> bool:
  lincol = len(A)
  for i in range(lincol):
    for j in range(lincol):
      if i > j:
        if (A[i][j] != 0):
          return False
  return True

def exercicio4(U:[[float]], b: [float]) -> [float]:
  for i in range(len(U)):
    if U[i][i] != 0:
      for j in range(len(b)):
        return U

def exercicio5(A: [[int]]) -> bool:
  nums = sorted(A[0])
  C = []
  for i in range(1,len(A)):
    nums2 = sorted(A[i])
    if nums != nums2:
      return False
  for j in range(len(A)):
    for k in range(len(A)):
      C.append(A[k][j])
      if (len(C) == 4):
        C.sort()
        if C != nums:
          return False
        C = []
  return True