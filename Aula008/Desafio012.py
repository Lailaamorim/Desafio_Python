#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Digite o preço: "))
desconto= preco-(preco * 5/100)
print(f"O preço do produto é {preco } e com o desconto foi para :{desconto}")