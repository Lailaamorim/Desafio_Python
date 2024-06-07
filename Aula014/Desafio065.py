#Cria um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# Inicialização das variáveis soma, cont, maior e menor
soma = cont = maior = menor = 0

# Loop infinito que só será interrompido quando o usuário inserir 0
while True:
    n = int(input("Insira um número [ou 0 para parar]: ")) 

    if n == 0:  # Verifica se o número inserido pelo usuário é 0
        break  # Se for 0, o loop é interrompido

    soma += n  # Adiciona o número inserido à variável soma
    cont += 1  # Incrementa o contador de números inseridos

    # Verifica se algum valor foi inserido para evitar divisão por zero
    if cont == 1:  # Se for o primeiro número inserido
        maior = menor = n  # Define o primeiro número como o maior e o menor
    else:
        # Se não for o primeiro número inserido, verifica se é o maior ou o menor
        if n > maior:
            maior = n  # Atualiza o maior número, se necessário
        if n < menor:
            menor = n  # Atualiza o menor número, se necessário

# Calcula a média dos números inseridos
media = soma / cont

# Exibe os resultados
print(f"Você digitou {cont} números. A média dos números é {media}, e a soma de todos os números é {soma}.")
print(f"O maior valor inserido é {maior} e o menor valor inserido é {menor}.")
