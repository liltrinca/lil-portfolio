def exercicio1(n: int) -> bool:
  k = len(str(n))
  med = k//2
  sr = 0
  sl = 0
  nstring = str(n)
  while med > 0:
    sr = sr + (n % 10)
    med -= 1
  med = k//2
  for i in range(0, med):
    sl = sl + int(nstring[i])
  return sl == sr

def exercicio2(m: int) -> int:
  top = 10**m
  bm = 0
  for i in range(0, top):
    if(exercicio1(i) == True):
      bm = bm + i
  return bm

def exercicio3(x: float) -> float:
  ans = 0
  for k in range(1,9):
    ans += (-1**(k+1))*((x**k)/k)
  return ans

def exercicio4(a:int,b:int,c:int,d:int,m:int,x: float) -> float:
  ans = 0
  G = [a,b]
  if(m >= 3):
    for i in range(2, m-1):
      value = c*G[i-1] + d*G[i-2]
      G.append(value)
  for j in range(0,m-1):
    ans += (x**m)*G[j]
  return ans

def exercicio5(p: float, n: int, k:int) -> float:
  def fat(n: int) -> int:
    f = 1
    for i in range(2, n+1):
      f *= i
    return f
  pcara, pcoroa = p, 1-p
  C = fat(n)/(fat(k)*fat(n-k))
  ans = C*(pcara**k)*(pcoroa**(n-k))
  return ans

def exercicio6(p: float, k: int) -> float:
  pcara, pcoroa = p, 1-p
  ans = pcara*(pcoroa**k)
  return ans

def exercicio7(p: float, n: int) -> int:
  import random
  pcara, pcoroa = p, 1-p
  ncaras = 0
  random.seed()
  a = random.uniform(pcara, pcoroa)
  problanc = a*n
  while(problanc > 1):
    ncaras += 1
    problanc -= 1
  return ncaras

def exercicio8(p: float, n: int, m: int) -> int:
  ncaraslanc = 0
  while (m != 0):
    ncaraslanc += exercicio7(p, n)
    m -= 1
  return ncaraslanc

def exercicio9(H:list) -> bool:
  k = len(H)-1
  n = H[len(H)-1]
  for j in range(1, k):
    if(H[j//2] <= H[j] and 2 >= j >= n):
      return False
  return True

def exercicio10(L:list, d: int) -> int:
  n = len(L)
  soma = 0
  i = 0
  somamant = 0
  if(0 <= d <= n):
    for j in range(1,n):
      if (i == 0):
        somaant = 0
      else:
        somaant = L[i] + L[i-1]
      soma = L[i] + L[j]
      if(soma > somaant and j-i >= d):
        somamant = soma
    return somamant