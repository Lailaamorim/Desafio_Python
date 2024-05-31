'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento de 15%.
'''

salario = float(input("Informe seu salário R$: "))

# Calcula o aumento de 10% e o novo salário para salários superiores a R$ 1250
if salario > 1250.00:
    aumento = salario * 10 / 100
    novo_salario = salario + aumento
    print(f"Seu aumento é de R${aumento:.2f}, totalizando R${novo_salario:.2f}")
# Se o salário for maior que R$ 1250, calcula o aumento de 10%

# Calcula o aumento de 15% e o novo salário para salários iguais ou inferiores a R$ 1250
else:
    aumento = salario * 15 / 100
    novo_salario = salario + aumento
    print(f"Seu aumento é de R${aumento:.2f}, totalizando R${novo_salario:.2f}")
# Se o salário for menor ou igual a R$ 1250, calcula o aumento de 15%
