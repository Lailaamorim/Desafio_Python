'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
para os inferiores ou iguais, o aumento de 15%.
'''
salario= float(input("Informe se salério R$: "))
salario_superior = salario * 10 / 100
total = salario + salario_superior
salario_inferior = salario * 15 / 100
total2 = salario + salario_inferior

#10%
if salario > 1250.00:
    print(f"O seu aumento é de R$ {salario_superior}, totalizando R$ {total} ")
else:#15%
    salario <= 1250.00
    print(f"O seu aumento é de R$ {salario_inferior}, totalizando R$ {total2}")

    