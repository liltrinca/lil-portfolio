def exercicio1(k: int) -> int:
  def checkp(n: int) -> bool:
    j, m = n, 0
    while j > 0:
      m = m * 10 + j % 10
      j = j//10
    return n == m

  maxk = (10**k)-1
  mink = 10**(k-1)
  a, b = maxk, maxk-1
  while b != mink-1:
    if(b == mink):
      b = maxk
      a -= 1
    else:
      b -= 1
    if(checkp(a*b) == True):
      ans = a * b
      break
  return ans

def exercicio2(n: int) -> int:
  def fat(n: int) -> int:
    f = 1
    for i in range(2, n+1):
      f *= i
    return f
  
  ans = fat(n*2)//fat(n)**2
  return ans

def exercicio3(A: list):
  m = 0
  istop = 0
  for i in range(len(A)):
    if(A[i] == 0):
      m += 1
      istop = i+1
      break
  for j in range(istop,len(A)):
    if(A[j] == 0):
      m += 1
    else:
      break
  return m,i,j

def exercicio4(n: int, m:int) -> int:
  A, ultpos = [], 0
  for i in range(n):
    A.append(i+1)
  for z in range(n-1):
    proxpop = (m-1) + ultpos
    if(proxpop >= len(A)):
      proxpop = len(A)-(proxpop)
    if(len(A) != 2):
      ultpos = (A.pop(proxpop))-1
    elif(n % 2 == 0):
      A.pop(1)
    else:
      A.pop(0)
  return A[0]

def exercicio5(A:list) -> int:
  ans = 0
  for i in range(len(A)):
    if(i == 0 and A[i] != A[i+1]):
      ans += 1
    elif(0 < i < len(A)-1 and A[i-1] != A[i] != A[i+1]):
      ans += 1
    elif(i == len(A)-1 and A[i] != A[i-1]):
      ans += 1
  return ans

def exercicio6(S: list, T:list) -> int:
  ans = 0
  mid = len(S)//2
  maxS = len(S)-1
  maxT = len(T)-len(S)+1
  for i in range(maxT):
    if(S[0] == T[i] and S[mid] == T[i+1] and S[maxS] == T[i+2]):
      ans += 1
  return ans

def exercicio7(A: list, L: list):
  cont = all(x in L for x in A)
  if (cont == True):
    return True
  return False

def exercicio8(A:list) -> list:
  B = []
  a = list(set(A))
  x, i = 0, 0
  while (len(B) != len(A)):
    if(a[i] == A[x]):
      B.append(x)
      i += 1
      x = 0
    else:
      x += 1
  return B
