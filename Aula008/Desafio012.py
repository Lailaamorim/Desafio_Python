#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço: "))
# Calcula o preço com desconto aplicando um desconto de 5%
desconto= preco-(preco * 5/100)
# Exibe o preço original do produto e o preço com desconto aplicado
print(f"O preço do produto é {preco } e com o desconto foi para :{desconto}")