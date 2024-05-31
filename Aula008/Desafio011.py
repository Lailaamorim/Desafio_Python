#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessário para pinta-lá, 
# sabendo que cada litro de tinta, pinta uma área de 2m^2

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

# Calcula a área da superfície multiplicando a largura pela altura
area = altura * largura

# Calcula a quantidade de tinta necessária, assumindo que 1 litro de tinta cobre 2 metros quadrados
tinta = area / 2

# Exibe a área calculada e a quantidade de tinta necessária para pintar essa área
print(f"Sua área é de {area} m² e você vai precisar de {tinta} litros de tinta.")

