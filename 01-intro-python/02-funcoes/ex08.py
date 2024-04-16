#Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como 
# argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores 
# são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes
# textos fornecidos pelo usuário.

frase = input("Digite uma frase: ")

def palavras(frase):  
    palavras = frase.split()
    dicionario_de_palavras = {}  
   
    for palavra in palavras: 
        dicionario_de_palavras[palavra] = dicionario_de_palavras.get(palavra, 0) + 1 #se já tiver a palavra vai adicionando 1
            
    print(dicionario_de_palavras)
    
print(palavras(frase))