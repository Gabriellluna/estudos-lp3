frase = input("Digite um trecho ou parágrafo: ")
frase = list(frase)


def caracteres(frase):
    for caractere in frase:
        if caractere == " ":
            frase.remove(caractere)
    contador = 0
    for item in frase:
        contador = contador + 1
    return f"O número de caracteres é: {contador}"
            
print(caracteres(frase))
    