#crie um programa que leia quanto dinheiro uma pessoa tem na arteira e 
#mostre quantos Dólares ela pode comprar

dol= float(input("Quantos Reais tem na sua carteira? "))
# Converte o valor de Reais para Dólares, usando uma taxa de câmbio fixa de 5.12 Reais por Dólar
total = dol / 5.12

print(f"Você consegue comprar {total} Dólares||| ")