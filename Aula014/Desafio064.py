#Cria um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição da parada. No final.
# mostra quantos números foram digitados a qual foi a soma entre elas (desconsiderando o Flag)
# (Flag é o número que força a parada do programa).



n = cont = soma = 0  # Inicializa as variáveis n, cont e soma com zero

while True:  # Loop infinito, que só será interrompido quando o comando break for executado
    n = int(input("Digite um número [999 para parar]: "))  # Solicita ao usuário que insira um número inteiro

    if n != 999:  # Verifica se o número inserido pelo usuário é diferente de 999
        cont += 1  # Incrementa o contador de números inseridos
        soma += n  # Adiciona o número inserido à soma total
    else:  # Se o número inserido for igual a 999, o loop é interrompido
        print(f"Você digitou {cont} números e a soma entre eles foi {soma}: ")  # Exibe o total de números inseridos e a soma deles
        break  # Interrompe o loop while


# Bem diferente da do professor 