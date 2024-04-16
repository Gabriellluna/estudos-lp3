frase = input("Digite uma frase: ")

def palavras(frase):
    for chave in palavras:  
        palavras[chave] = frase.split()
        print(palavras)
    
 
palavras(frase)