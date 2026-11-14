# Receba nome, cargo e salário e acrescente 10%.

# entrada
nome = input("Qual é o seu nome ? ")
cargo = input("Qual é o seu cargo ? ")
salario = float(input("Quanto você recebe ? "))
porcentagem = 0.1
# processamento
soma1 = salario * porcentagem
soma2 = soma1 + salario

# saída

print(f"{nome} você possui o cargo {cargo} e seu salário teve um acrecimo de 10%, o seu salário atual é {soma2} R$")