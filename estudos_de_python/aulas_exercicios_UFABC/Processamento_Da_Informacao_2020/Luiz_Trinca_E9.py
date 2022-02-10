def exercicio1(A: list[list[float]]) -> list[float]:
  vec = []
  for i in range(len(A)):
    for j in range(len(A[0])):
      vec.append(A[i][j])
  return vec

def exercicio2(A:list[list[float]]) -> bool:
  n = len(A)
  for i in range(n):
    for j in range(n):
      if(A[i][i] < A[i][j]):
        return False
  return True

def exercicio3(A:list[list[int]]) -> bool:
  for i in range(len(A)):
    has1 = 0
    for j in range(len(A)):
      if (A[i][j] == 1):
        has1 += 1
      if (has1 != 1):
        return False
  return True

print(exercicio3([[0,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,0]]))

def exercicio4(A:list[list[float]],B:list[list[float]]) -> list[list[float]]:
  alin, acol, blin, bcol = len(A), len(A[0]), len(B), len(B[0])
  reslin = alin * blin
  rescol = acol * bcol
  res = []
  for i in range(reslin):
    res.append([])
  for m in range(alin):
    for n in range(acol):
      escalar = A[m][n]
      for o in range(blin):
        for p in range(bcol):
          mult = escalar * B[o][p]
          res[m].append(mult)
  return res
