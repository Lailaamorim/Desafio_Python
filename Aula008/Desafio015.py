#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos 
#quais ele foi alugado e calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#day = int(input("Quantos dias Alugado? "))
#km = int(input("Quantos KM Rodados? "))
#print(f"O valor dos dias alugados é de R$ {day*60}, o valor de KM rodado é de R${km*0.15} o valor total a pagar é R$ {(day*60)+(km*0.15)} ")

# Solicita ao usuário que insira a quantidade de dias que o carro foi alugado e converte a entrada para um valor float
day = float(input("Quantos dias alugados? "))

# Solicita ao usuário que insira a quantidade de quilômetros rodados e converte a entrada para um valor float
km = float(input("Quantos km rodados? "))

# Calcula o custo total dos dias alugados, assumindo que o custo é de R$ 60,00 por dia
alu = day * 60

# Calcula o custo total dos quilômetros rodados, assumindo que o custo é de R$ 0,15 por quilômetro
rod = km * 0.15

# Calcula o custo total somando o custo dos dias alugados e o custo dos quilômetros rodados
total = alu + rod

# Exibe o valor dos dias alugados, o valor dos quilômetros rodados e o custo total
print(f"O valor dos dias alugados é de R$ {alu}, o valor dos km rodados é de R$ {rod}, o total é de R$ {total}")
