#Exercício 4
candidatos = {
                "Gabriel" : [[], []],
                "Marcos" : [[], []],
                "Bobley" : [[], []]
            }

def votacao(candidatos):
    i = 1
    while i < 6:
        print("Candidatos: Gabriel(22), Marcos(13), Bobley(70)\n")
        voto = int(input("Insira o número do candidato: "))
        match voto:
            case 22:
                candidatos["Gabriel"][0].append(i)
                candidatos["Gabriel"][1] = len(candidatos["Gabriel"][0])
            case 13:
                candidatos["Marcos"][0].append(i)
                candidatos["Marcos"][1] = len(candidatos["Marcos"][0])
            case 70:
                candidatos["Bobley"][0].append(i)
                candidatos["Bobley"][1] = len(candidatos["Bobley"][0])
            case _:
                print("Número inválido")
        i = i + 1   
    
    percorre(candidatos)
    eleito(candidatos)
    
     
def percorre (candidatos):
    for chave in candidatos.keys():
        print(f'Candidato = {chave} | Votos = {candidatos[chave][1]}')
    
def eleito (candidatos):
    maior = []
    for chave in candidatos.keys():
        maior.append(candidatos[chave][1])
        maiorzao = max(maior)
    if maiorzao is maior[0] and maiorzao is maior[1] or maiorzao is maior[1] and maiorzao is maior[2] or maiorzao is maior[0] and maiorzao is maior[2]:
        print("EMPATE")
           
    else:
            
        for chave in candidatos.keys():    
            if maiorzao is candidatos[chave][1]:
                print(f"Vencedor: {chave} ")
                break
       

print(votacao(candidatos))