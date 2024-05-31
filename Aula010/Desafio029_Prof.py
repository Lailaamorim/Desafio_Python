'''Escreva um programa que leia a velocidade de um carro.'''

'''Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acimado limite.'''

velocidade = float(input("Qual a velocidade atual do carro? "))

if velocidade > 80:# Verifica se a velocidade é maior que 80 km/h
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")# Se a velocidade exceder 80 km/h, imprime uma mensagem de multa
    multa = (velocidade - 80) * 7 # Calcula o valor da multa com base na velocidade excedente
    print(f"Você deve pagar uma multa de R$ {multa}")# Exibe o valor da multa que o motorista deve pagar
    
print("Tenha um bom dia! Dirija com segurança!")
# Independente da velocidade, deseja ao motorista um bom dia e lembra-o de dirigir com segurança