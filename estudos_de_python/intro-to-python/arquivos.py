#Manipulação de arquivos
#open(nome, modo)
#modo r -> somente leitura
#modo w -> escrita (apaga o conteúdo anterior do arquivo)
#modo a -> leitura e escrita (adiciona o conteudo ao fim do arquivo)
#modo r+ -> leitura e escrita
#modo w+ -> escrita(apaga o conteúdo anterior do arquivo)
#modo a+ -> leitura e escrita(abre o arquivo para atualização)

arquivo = open("intro-to-python\\arquivo.txt")
texto = arquivo.read()
arquivo.close()

print(texto)

#readlines() -> lê linhas e converte em lista
#read -> lê o texto e converte em string

w = open("intro-to-python\\arquivo2.txt", "w")

w.write("Esse e o meu arquivo 2")
w.close()

a = open("intro-to-python\\arquivo.txt", "a")
a.write("\nAdicionando uma nova linha\n")
a.close()