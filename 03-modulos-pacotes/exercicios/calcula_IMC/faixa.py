#Classificação
#----------------------------------
#IMC           Classificação
#-----------------------------------
#< 18,5             Baixo peso
#18,5 a 24,9     Peso normal
#25,0 a 29,9     Excesso de peso
#30,0 a 34,9     Obesidade de Classe 1
#35,0 a 39,9     Obesidade de Classe 2
#>= 40,00         Obesidade de Classe 3


def classificacao(numero):
    if numero <= 18.5:
        print("Baixo peso")
    elif numero <= 24.9:
        print("Peso normal")
    elif numero <= 29.9:
        print("Excesso de peso")
    elif numero <= 34.9:
        print("Obesidade de Classe 1")
    elif numero <= 39.9:
        print("Obesidade de Classe 2")
    else:
        print("Obesidade de Classe 3")
    