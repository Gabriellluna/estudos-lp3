#Exercício 2
numero = int(input("Insira um número para ver sua tabuada: "))

def tabuada (numero):
    i = 1
    for i in range(1,11):
        produto = numero * i
        print(f'{numero} X {i} = {produto}')
        i = i + 1
tabuada(numero)