#Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos 
#quais ele foi alugado e calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#day = int(input("Quantos dias Alugado? "))
#km = int(input("Quantos KM Rodados? "))
#print(f"O valor dos dias alugados é de R$ {day*60}, o valor de KM rodado é de R${km*0.15} o valor total a pagar é R$ {(day*60)+(km*0.15)} ")

day =float(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))

alu= (day*60)
rod = (km*0.15)
total = (alu+rod)


print(f"o valor dos dias alugados é de R$ {alu}, o valor dos km rodados é de R${rod}, o total é de R$ {total}")