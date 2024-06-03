#Cria um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição da parada. No final.
# mostra quantos números foram digitados a qual foi a soma entre elas (desconsiderando o Flag)
# (Flag é o número que força a parada do programa).

n = cont = soma = 0
while True: 
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        cont += 1
        soma += n
    elif n == 999:
        print(f"Você digitou {cont} números e a soma entre eles foi {soma}: ")  
        break  

# Bem diferente da do professor 