#A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o 
# cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
from calcula_AQUARIO import volume


def calculadora(comprimento, altura, largura, temperatura1, temperatura2):
    volum = volume.calculadora(comprimento, altura, largura)
    return((volum * 0.05 * (temperatura1 - temperatura2)))