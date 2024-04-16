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