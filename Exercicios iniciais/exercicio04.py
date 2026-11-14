# Receba nome, peso e altura. Calcule IMC.

# Entrada
nome = input("Digite o seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))

# Processamento

imc = peso / altura**2

# Saida

print(f"{nome} o seu imc é: {imc:2f}")