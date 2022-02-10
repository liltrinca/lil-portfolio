#conjunto de chave-valor, assim como em JS

dicionario = {
    "A": "Ameixa",
    "B": "Banana",
    "C": "Cachorro"
}

print(dicionario)
print(dicionario["A"])

for chave in dicionario:
    print(chave + ": " + dicionario[chave])

#Converte o dicionário em tupla
for i in dicionario.items():
    print(i)

#Retorna valores
for i in dicionario.values():
    print(i)

#Retorna keys
for i in dicionario.keys():
    print(i)