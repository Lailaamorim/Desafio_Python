#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessário para pinta-lá, 
# sabendo que cada litro de tinta, pinta uma área de 2m^2

largura= float(input("Digite a largura: "))
altura=float(input("Digite a altura: ")) 
area = (altura * largura) 
tinta = area/2
print(f"sua area é de {area} e você vai precisar de {tinta},tinta")
