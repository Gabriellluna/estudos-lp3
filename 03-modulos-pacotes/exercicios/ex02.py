#Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

#IMC = peso / altura * altura



from calcula_IMC import IMC, faixa

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

print("O seu IMC é igual a: " , IMC.calculadora(peso, altura))
faixa.classificacao(IMC.calculadora(peso, altura))



