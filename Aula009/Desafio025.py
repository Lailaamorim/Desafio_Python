#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = input("Qual o seu nome completo? ")
print(f"Seu nome tem Silva? {('SILVA'in nome.upper())}") #Quer saber se 'SILVA'esta dentro de nome  => usa o operador 'in'