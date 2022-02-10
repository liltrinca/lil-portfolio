from functools import reduce

#lista = [valor_a_adicionar_na_lista for valor in (condição)]
def listComprehension(x: list) -> list:
    y = [i**2 for i in x]
    z = [i for i in x if i%2==1]
    print(y)
    print(z)

#numerar valores em uma lista
def funcEnumerate(x: list):
    for i, value in enumerate(x):
        print(i, value)

#realiza certa função em diversos valores de uma vez
def funcMap(iterableList: list) -> list:
    def dobro(x: int) -> int:
        return x*2
    
    returnmap = list(map(dobro, iterableList)) #Precisamos converter em lista pois map retorna um objeto map
    return returnmap

#retorna um único valor de uma lista a partir de uma função, parecido com map()
def funcReduce(x: list) -> int:
    def soma(x, y):
        return x + y
    
    soma = reduce(soma, x)
    return soma

#concatena listas adicionando elemento a partir de elemento
def funcZip(x: list, y: list) -> list:
    for i, j in zip(x, y):
        print(i, j)

funcZip([1,2,3,4,5], ["porra","cu","teste2","teste3","teste4"])