# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

#ex: Digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1

num = int(input("Digite um número: "))

u = num // 1 % 10
# Calcula a unidade do número: divide o número por 1 e pega o resto da divisão por 10
d = num // 10 % 10
# Calcula a dezena do número: divide o número por 10 e pega o resto da divisão por 10
c = num // 100 % 10
# Calcula a centena do número: divide o número por 100 e pega o resto da divisão por 10
m = num // 1000 % 10
# Calcula o milhar do número: divide o número por 1000 e pega o resto da divisão por 10

print(f"Analisando o número {num} ...")
print(f"Unidade: {u}")
print(f"Dezena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")
# Exibe o número analisado e cada um de seus dígitos separadamente (unidade, dezena, centena e milhar)
