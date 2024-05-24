'''Escrava um programa que leia dois números inteiros a compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior - O segundo valor é menor - Não existe valor maior, os dois são iquais'''

valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
if valor1 > valor2:    
    print(f"O primeiro valor {valor1} é o maior, e o valor {valor2} é o menor")
elif valor2 > valor1:
    print(f"O segundo valor {valor2} é maior, e o valor {valor1} é o menor")
elif valor1 == valor2:
    print("Não existe valor maior, os dois são iquais")    