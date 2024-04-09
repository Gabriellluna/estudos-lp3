  
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
frase2 = frase.lower()
vogais = 0
consoantes = 0

def contador(frase):
    vogal = ('a', 'e', 'i', 'o', 'u')
    consoante = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    vogais = 0
    consoantes = 0
    for char in frase:
        if char in vogal:
           vogais = vogais + 1
        elif char in consoante:
            consoantes = consoantes + 1
    return f"O número de consoantes da frase é: {consoantes}. O de vogais é: {vogais}"          

print(contador(frase2))

#Exercício 4
candidatos = {
                "Bolsonaro - 22" : [],
                "Lula - 13" : [],
                "Bob Marley - 69" : []
            }
print("antes: ",candidatos)
def votacao(candidatos):
    i = 1
    while i < 11:
        voto = int(input("Insira o número do candidato: "))
        match voto:
            case 22:
                candidatos["Bolsonaro - 22"].append(i)
            case 13:
                candidatos["Lula - 13"].append(i)
            case 69:
                candidatos["Bob Marley - 69"].append(i)
            case _:
                print("Número inválido")
        i = i + 1        
                
    return f"depois: {candidatos}"
       
def eleito(candidatos):
    for candidato, votos in candidatos.items():
        numero_de_votos = len(votos)
        print(f"{candidato}: {numero_de_votos} votos")            

print(votacao(candidatos))
eleito(candidatos)