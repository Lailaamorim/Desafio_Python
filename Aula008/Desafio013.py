#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto
salario = float(input("Digite o salario: "))
desconto= salario+(salario* 15/100)
print(f"O preço do produto é {salario} e com o desconto foi para :{desconto}")