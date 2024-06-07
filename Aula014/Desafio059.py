#Crie um programa que leia dois valores a mostre um menu na tela:
'''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

#inicia com dois valores  

valor1 = int(input("Primeiro número: "))  
valor2 = int(input("Segundo número: "))  

# Loop infinito para exibir o menu até que o usuário escolha sair
while True:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    
    opção = int(input("Escolha uma opção: "))  # Lê e converte a opção escolhida pelo usuário para um inteiro
    
    # Verifica a opção escolhida pelo usuário
    if opção == 1:
        # Soma os dois valores e exibe o resultado
        s = valor1 + valor2  # Calcula a soma dos dois números
        print(f"Soma: {valor1} + {valor2} = {s}") 
        
    elif opção == 2:
        # Multiplica os dois valores e exibe o resultado
        m = valor1 * valor2  # Calcula o produto dos dois números
        print(f"Multiplicação: {valor1} * {valor2} = {m}")  # Exibe o resultado da multiplicação
        
    elif opção == 3:
        # Determina qual dos dois valores é maior e exibe o resultado
        if valor1 > valor2:
            maior = valor1  # Se valor1 é maior que valor2, armazena valor1 em 'maior'
        else:
            maior = valor2  # Se valor2 é maior ou igual a valor1, armazena valor2 em 'maior'
        print(f"Valor Maior é: {maior}")  # Exibe o maior valor
            
    elif opção == 4:
        # Permite ao usuário inserir novos valores para as variáveis
        valor1 = int(input("Primeiro número: "))  # Lê e converte um novo valor para 'valor1'
        valor2 = int(input("Segundo número: "))   # Lê e converte um novo valor para 'valor2'
        
    elif opção == 5:
        # Sai do loop e encerra o programa
        print("Saindo do Programa!!") 
        break  # Interrompe o loop infinito
    else:
        # Informa ao usuário que a opção escolhida é inválida
        print("Opção inválida")  # Exibe uma mensagem de erro se a opção não for válida

