'''Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, 
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. '''

distancia = float(input("Qual a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia} km.")
# Exibe uma mensagem informando a distância da viagem
if distancia <= 200:
    # Verifica se a distância da viagem é menor ou igual a 200 km
    preco = distancia * 0.50
    # Se a distância for menor ou igual a 200 km, calcula o preço da passagem multiplicando a distância por R$ 0.50
else:
    preco = distancia * 0.45
    # Se a distância for maior que 200 km, calcula o preço da passagem multiplicando a distância por R$ 0.45

print(f"O preço da sua passagem será de R${preco:.2f}")
# Exibe o preço da passagem com duas casas decimais

