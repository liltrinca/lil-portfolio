a = "Diego"
b = "Mariano"

concatenar = a + " " + b
print(concatenar)

#Tamanho de uma string
print(len(concatenar))

#Caracter na posição
print(a[2])

#Sequencia de caracteres
print(concatenar[0:5])

#Aplicando metodos em Strings
seq = "CGATC AGATAG CAGA CAG T "
print(seq.lower())
print(seq.upper())

#Removendo espaços no começo e no fim da String
print(seq.strip())

#Função Split
teste1 = "O rato roeu a roupa do rei de roma"
lista = teste1.split(" ")
print(lista)

#Função find
busca = teste1.find("rei")

print(busca)
print(teste1[busca:]) #Buscando e printando todos dentro do array

#Função Replace
replaced = teste1.replace("o rei", "a rainha")
print(replaced)