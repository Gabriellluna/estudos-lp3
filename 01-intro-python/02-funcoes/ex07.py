#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma 
# palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. 
# O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

palavra = "ANA"
palavra = palavra.lower()
lista = list(palavra)
letra_usuarios = []
#ganhou = letra_usuarios != lista
tentativas = 1



def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

def verifica(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    return conjunto1 == conjunto2



def jogar(letra, tentativas):
    while not(verifica(remove_repetidos(lista), letra_usuarios)) and tentativas < 8:
        letra_usuarios.append(input("Insira uma letra: "))
        palavra_descoberta = ''
        for letra_palavra in palavra:
            if letra_palavra in letra_usuarios:
                palavra_descoberta += letra_palavra
            else:
                palavra_descoberta += '_'
        print(palavra_descoberta)           
        print(f"Tentativas: {tentativas}")
        tentativas = tentativas + 1 


    if tentativas == 8 and not(verifica(remove_repetidos(lista), letra_usuarios)) == False:
        print(f"Você ganhou, parabéns. A palavra era: {palavra.upper()}")
    elif tentativas == 8:
        print(f"Você atingiu o número máximo de tentativas. A palavra era: {palavra.upper()}")
    else:
        print(f"Você ganhou, parabénss. A palavra era: {palavra.upper()}")
        
jogar(letra_usuarios, tentativas)

