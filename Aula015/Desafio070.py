'''
Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai 
continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.
'''
total = totmil = menor = cont = 0  # Inicializa as variáveis total, totmil, menor e cont com zero
barato = ''  # Inicializa a variável barato como uma string vazia

while True:  # Loop infinito para permitir que o usuário continue adicionando produtos
    produto = input("Nome do produto: ")  # Solicita ao usuário o nome do produto
    preço = float(input('Preço: R$ '))  # Solicita ao usuário o preço do produto
    
    cont += 1  # Incrementa o contador de produtos
    total += preço  # Adiciona o preço do produto ao total
    
    if preço > 1000:  # Verifica se o preço do produto é maior que R$ 1000
        totmil += 1  # Incrementa o contador de produtos com preço maior que R$ 1000
    
    if cont == 1 or preço < menor:  # Verifica se é o primeiro produto ou se o preço é menor que o menor preço registrado até agora
        menor = preço  # Atualiza o menor preço registrado
        barato = produto  # Atualiza o nome do produto mais barato
    
    resp = ''  # Inicializa a variável resp como uma string vazia
    
    # Loop enquanto a resposta não for 'S' ou 'N'
    while resp not in "SN":
        resp = input("Quer continuar [S/N] ").strip().upper()[0]  # Pergunta ao usuário se deseja continuar adicionando produtos
    
    if resp == "N":  # Se a resposta for 'N', o loop é interrompido e o programa termina
        break 

print("FIM DO PROGRAMA")
print(f"O total da compra foi R$ {total:.2f}")  # Exibe o total da compra com duas casas decimais
print(f"Temos {totmil} produto(s) custando mais de R$ 1000.00")  # Exibe o número de produtos com preço maior que R$ 1000
print(f"O produto mais barato custa R$ {menor:.2f}")  # Exibe o preço do produto mais barato com duas casas decimais
