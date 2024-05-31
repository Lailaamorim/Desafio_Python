#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto
salario = float(input("Digite o salario: "))
# Calcula o novo salário com um aumento de 15%
desconto= salario+(salario* 15/100)
# Exibe o salário original e o novo salário após o aumento
print(f"O preço do produto é {salario} e com o desconto foi para :{desconto}")