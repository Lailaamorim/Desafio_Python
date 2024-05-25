'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
O programa vai perguntar o valor da casa, o salário do comprador a am quantos anos ale vai pagar.
Calcule o valor da prestação mensal. sabendo que ela não pode exceder 30% do MAIS VIDEOS então o 
empréstimo será nagado.
Infelismente vc não pode finaciar essa casa
'''

casa = float(input("Valor da casa: R$ "))
salário = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento? "))

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print(f"Para pagar uma casa de {casa:.2f}, em {anos} anos ")
print(f"A prestação será de R$ {prestação:.2f}")
if prestação <= mínimo:
    print("Emprestimo pode ser CONCEDIDO!")
else:
    print("Emprestimo NEGADO!")