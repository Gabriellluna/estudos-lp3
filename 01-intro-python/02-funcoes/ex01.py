  
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
        
verifica(numero1, numero2)




    
    


