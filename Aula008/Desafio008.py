#Escreva um programa que leia um valor em metros e o 
#exiba convertido em centimetros e milimetros

num1 = float(input("Digite o primeiro numero para ser convertido: "))

cem = num1 * 100  # Converte o número para centímetros (multiplicando por 100)
mil = num1 * 1000 # Converte o número para milímetros (multiplicando por 1000)

print(f"O número {num1} Convertido em centimetros é {cem} e convertido em milimetro é {mil}")