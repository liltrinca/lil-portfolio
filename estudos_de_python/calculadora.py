def soma(a: int, b: int) -> int:
    print(a + b)

def subtracao(a: int, b: int) -> int:
    print(a - b)

def multiplicacao(a: int, b: int) -> int:
    print(a * b)

def divisao(a: int, b: int) -> int:
    if (b != 0):
        print(a / b)
    else:
        print("Can't Divide by Zero!")

stay = ""

while (stay != "N" and stay != "n"):
    firstElement = int(input("Insira o primeiro elemento"))
    operator = input("Insira o operador")
    secondElement = int(input("Insira o segundo elemento"))   
    if (operator == "+"):
        soma(firstElement, secondElement)
    elif (operator == "-"):
        subtracao(firstElement, secondElement)
    elif (operator == "*"):
        multiplicacao(firstElement, secondElement)
    elif (operator == "/"):
        divisao(firstElement, secondElement)
    stay = input("Deseja continuar na calculadora? S/N")
