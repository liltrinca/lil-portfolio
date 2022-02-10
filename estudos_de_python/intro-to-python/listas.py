minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]

for item in minha_lista:
    print(item)

#tamanho da lista
tamanho = len(minha_lista)
print(tamanho)

#adicionando elementos
minha_lista.append("limao")
print(minha_lista)

#verificando se existe na linha
if 3 in minha_lista_2:
    print("3 esta na lista")

#removendo elementos da lista
del minha_lista[2:]
print(minha_lista)

#apagando toda a lista
del minha_lista[:]
print(minha_lista)

#ordenando lista
lista = [123, 512, 5, 2, 3, 1265, 235, 1, 0]
a = sorted(lista) #retorna a lista ordenada mas não altera a lista padrão
lista.reverse() #inverte a lista sem ordenar
print(lista)
lista.sort() #altera a lista padrão
print(lista)
print(a)

lista.sort(reverse=True) #ordena ao contrário
print(lista)

#também é possível ordenar alfabéticamente com strings