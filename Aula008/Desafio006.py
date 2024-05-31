# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

# Solicita ao usuário que insira um número e o converte para inteiro
num = int(input("Digite um número:"))


dobro = num * 2# Calcula o dobro do número
triplo = num * 3# Calcula o triplo do número
raiz =  num ** (1/2) #Calcula a raiz quadrada do número

# Imprime o resultado do dobro, triplo e raiz quadrada do número
print(f"O dobro de {num} vale {dobro}.")
print(f"O triplo de {num} vale {triplo}. A raiz quadrada é: {raiz}.")


