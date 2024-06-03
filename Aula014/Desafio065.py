#Cria um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = cont = maior = menor = 0

while True:
    n = int(input("Insira um número [ou 0 para parar]: "))
    if n == 0:
        break
    soma += n 
    cont += 1
# Verifica se algum valor foi inserido para evitar divisão por zero
    #maior ou menor
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont   
print(f"Você digitou {cont }A média dos números é {media}, a soma de todos os números é {soma}")   
print(f"O Maior valor inserido é {maior} e o Menor valor inserido é {menor} ") 
