'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, 
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. '''

distancia= float(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia}km.")
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da sua passagem será de R${preco:.2f}")        

