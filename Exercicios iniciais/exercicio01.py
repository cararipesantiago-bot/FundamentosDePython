# 1. Receba a idade em anos e imprima em meses, dias, horas e minutos.

# entrada
idade = int(input("Digite a idade: ")) # converte o texto para número

# Processamento

idadeEmMeses = idade * 12
idadeEmDias = idade * 365
idadeEmHoras = idadeEmDias * 24
idadeEmMinutos = idadeEmHoras * 60

# Saida

print(f'A idade em meses é: {idadeEmMeses} meses')
print(f'A idade em dias é: {idadeEmDias} dias')
print(f'A idade em horas é: {idadeEmHoras} horas')
print(f'A idade em minutos é: {idadeEmMinutos} minutos')