  
#Exercício 1
numero1= int(input("Insira o número: "))
import random
numero2 = random.randint(1,100)

def verifica (numero1, numero2):
    while(numero2 is not numero1):
        if (numero1 > numero2):
            print("O plapite está alto")
            numero1= float(input("Insira outro número: "))   
        elif (numero1 < numero2):
            print("O plapite está baixo")
            numero1= float(input("Insira outro número: "))   
        else:
            print("Acertou")
            break
        
#verifica(numero1, numero2)


#Exercício 2
numero = int(input("Insira um número para ver sua tabuada: "))
i = 1
for i in range(1,11):
    print(numero * i)
    i = i+1
    
    
#Exercício 3
frase = input("Digite algo: ")
frase2 = frase.strip()
print(frase2)
for char in frase:
    print(char)
print(type(frase))
print(type(frase2))


#Exercício 4
voto = int(input("Insira o número do candidato: "))
i = 1
#for i < 50: