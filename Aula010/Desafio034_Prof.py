salario = float(input("Qual é o salário do funcionário? R$ "))
if salario <= 1250:
    # Verifica se o salário é menor ou igual a R$ 1250
    novo = salario + (salario * 15 / 100)
    # Se o salário for menor ou igual a R$ 1250, calcula o novo salário com um aumento de 15%
else:
    novo = salario + (salario * 10 / 100)
    # Se o salário for maior que R$ 1250, calcula o novo salário com um aumento de 10%

print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novo:.2f} agora.")
# Exibe o salário anterior e o novo salário com duas casas decimais
