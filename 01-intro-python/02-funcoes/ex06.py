#Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
# converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
#a => 90
#b => 80
#c => 70
#d => 60
#else
#f

nota = float(input(print("Insira sua nota aqui (de 0 a 100): ")))
letra = ""
def nota_em_letra(nota, letra):
    if nota >= 90:
        letra = "A"
        return f"Sua nota {nota} foi convertida para {letra}"
    elif nota >= 80:
        letra = "B"
        return f"Sua nota {nota} foi convertida para {letra}"
    elif nota >= 70:
        letra = "C"
        return f"Sua nota {nota} foi convertida para {letra}"
    elif nota >= 60:
        letra = "D"
        return f"Sua nota {nota} foi convertida para {letra}"
    else:
        letra = "F"
        return f"Sua nota {nota} foi convertida para {letra}"

print(nota_em_letra(nota, letra))