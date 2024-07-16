#Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as 
# seguintes informações.

#O volume do aquário em litros;
#A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
#A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
#Volume é dado por (comprimento * altura * largura) / 1000
#A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
#A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.
from calcula_AQUARIO import volume
from calcula_AQUARIO import potencia


comprimento = float(input("Insira o comprimento do seu aquário: "))
altura = float(input("Insira a altura do seu aquário: "))
largura = float(input("Insira a largura do seu aquário: "))
temperatura = [1, 2]
temperatura[0] = float(input("Insira a temperatura desejada no aquário: "))
temperatura[1] = float(input("Insira a temperatura ambiente atual: "))


print("O volume do seu aquário é igual a: ", volume.calculadora(comprimento, altura, largura))
print("A potência necessária para manter a temperatura adequada dentro do aquário é: ", 
      potencia.calculadora(comprimento, altura, largura, temperatura[0], temperatura[1])
      )
print(f"Quantidade de filtragem por hora necessária: entre {volume.calculadora(comprimento, altura, largura) * 2:.2f} e {volume.calculadora(comprimento, altura, largura) * 3:.2f} litros")


