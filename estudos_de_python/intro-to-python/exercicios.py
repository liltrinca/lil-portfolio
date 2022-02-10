from math import sqrt

#Exercício 1
def exercicio1 ():
    def isUnderAge (age: int) -> str:
        if (age < 18):
            return "Menor de idade"
        else:
            return "Maior de idade"

    try:
        userAge = int(input("Insira sua idade"))
        print(isUnderAge(userAge))
    except:
        print("Insira um valor numérico!")
#Exercício 1

#Exercício 2
def exercicio2 ():
    def isApproved(a: int, b: int) -> bool:
        median = (a + b) / 2
        if (median < 6): return False
        else: return True
    try:
        grade1 = int(input("Insira a primeira nota: "))
        grade2 = int(input("Insira a segunda nota: "))
        if (isApproved(grade1, grade2)): print("Aprovado")
        else: print("Reprovado")
    except:
        print("Insira um valor numérico")
#Exercício 2

#Exercício 3
def exercicio3(a: float, b: float, c: float):
    try:
        delta = (b**2) - (4*a*c)
        if (delta < 0):
            print("Delta menor que zero, inexiste raiz real")
        elif (delta == 0):
            xzero = (-b) / (2*a)
            print("Só existe uma solução para x: ", xzero)
        elif (delta > 0):
            xone = ((-b) + sqrt(delta)) / (2*a)
            xtwo = ((-b) + sqrt(delta)) / (2*a)
            print("Existem duas soluções para x: ", xone, xtwo)
    except:
        print("Um dos valores não é numérico!")
#Exercicio 3

#Exercicio 4
def exercicio4(sortList: list[int]) -> list:
    return sorted(sortList)
#Exercicio 4

#Exercicio 5
def exercicio5():
    a = float(input("Insira o primeiro valor: "))
    operator = input("Insira o operador: ")
    b = float(input("Insira o segundo valor: "))  

    def validateOperation(operator: str, a: float, b: float) -> float:
        if (operator == "+"):
            return a + b
        if (operator == "-"):
            return a - b
        if (operator == "*"):
            return a * b
        if (operator == "/"):
            return a / b 

    print(validateOperation(operator, a, b))
#Exercicio 5