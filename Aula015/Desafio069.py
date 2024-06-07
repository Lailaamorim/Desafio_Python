'''
Cria um programa que leia a idade e o saxo de várias pessoas. A cada pessoa cadastrada, o programa deverá 
perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20.

'''
tot18 = totH = totM20 = 0  # Inicializa as variáveis tot18, totH e totM20 com zero

while True:  # Loop infinito para permitir que o programa continue rodando até que seja interrompido
    idade = int(input("Idade: ")) 
    
    sexo = ' '  # Inicializa a variável sexo como um espaço em branco
    
    # Loop enquanto o sexo não for 'M' ou 'F'
    while sexo not in 'MF':
        sexo = input("Sexo: [M/F] ").strip().upper()[0]  # Solicita ao usuário que informe o sexo
    
    # Contagem de pessoas com mais de 18 anos
    if idade >= 18:
        tot18 += 1
    
    # Contagem de homens cadastrados
    if sexo == 'M':
        totH += 1 
    
    # Contagem de mulheres com menos de 20 anos
    if sexo == "F" and idade < 20:
        totM20 += 1   
    
    resp = ' '  # Inicializa a variável resp como um espaço em branco
    
    # Loop enquanto a resposta não for 'S' ou 'N'
    while resp not in "SN":
        resp = input("Quer continuar? [S/N] ").strip().upper()[0]  # Pergunta ao usuário se deseja continuar cadastrando
    
    if resp == 'N':  # Se a resposta for 'N', o loop é interrompido e o programa termina
        break

# Exibe os resultados
print(f"Total de pessoas com mais de 18 anos: {tot18}")    
print(f"Ao todo temos {totH} homens cadastrados")
print(f"E temos {totM20} mulheres com menos de 20 anos")
