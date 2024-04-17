#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique 
# se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

frase = input("Insira uma palavra: ")




def inverte(frase):
    original = list(frase.lower())
    for palavra in frase:
        if palavra == " ":
            original.remove(palavra)
    invertido = list(frase[::-1].lower())
    for palavra in invertido:
        if palavra == " ":
            invertido.remove(palavra) 
    verificacao(original, invertido)
  
            
def verificacao(original, invertido):
    if original == invertido:
        print("É um anagrama")
    else:
        print("Não é um anagrama")
        
inverte(frase)

