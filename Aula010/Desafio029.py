'''Escreva um programa que leia a velocidade de um carro.'''

'''Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acimado limite.'''

# Definindo o limite de velocidade

velocidade= float(input("Digite a velocidade do carro (Km/h): "))
execesso_velocidade = velocidade - 80
multa= execesso_velocidade * 7.0
if velocidade > 80: # utilizamos só o if, é o que chamamos de condição simples
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km/h Você tem que pagar uma multa de R$ {multa:.2f}")
print("Tenha um bom dia! Dirija com segurança")    
