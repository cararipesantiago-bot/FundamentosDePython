# Receba ano de nascimento e ano atual. Calcule idade e semanas.

# entrada
anoDeNascimento = int(input("Digite o ano de nascimento: ")) # converte o texto para número
anoAtual = int(input("Digite o ano atual: ")) # converte o texto para número

# Processamento
idade = anoAtual - anoDeNascimento
semana = idade * 4 * 12


# Saida
print(f'Sua idade é: {idade}')
print(f'Sua idade em semanas é: {semana}')