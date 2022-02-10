a = 2
b = 0

try:
    print(a/b)
except:
    print("Nao e permitida divisao por 0")

print(a/a)

#Caso aconteça algum erro, o python trata o erro e continua com a execução do programa
#Isso acontece usando try, except