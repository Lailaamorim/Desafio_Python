'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual 
foi a soma entre eles  (Desconsiderando o flag)
'''
s = cont = 0  # Inicializa as variáveis s (soma) e cont (contador) com zero

while True:  # Loop infinito que só será interrompido quando o usuário inserir 999
    n = int(input("Insira um valor [999 para parar]: "))  # Solicita ao usuário que insira um valor inteiro

    if n == 999:  # Verifica se o valor inserido pelo usuário é 999
        break  # Se for 999, o loop é interrompido

    cont += 1  # Incrementa o contador de valores inseridos
    s += n  # Adiciona o valor inserido à soma

# Exibe a soma dos valores e a quantidade de valores inseridos
print(f"A soma dos {cont} valores é {s}.")
