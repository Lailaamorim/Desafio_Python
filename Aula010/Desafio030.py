'''Crie um programa que leia um número inteiro e mostre na tela se ele é Par ou impar.'''
numero =int(input("Digite um número para saber se é par ou impar: "))
if numero % 2 == 0:
    print(f"O número {numero} é Par!")
else:
    print(f"O número {numero} é Impar!")    
    
    #Todo número par vai dar resultado '0' o resto da divisão de qualquer número par por 2 é '0'
    #Todo número impar vai dar resultado '1' o resto da divisão de qualquer número impar por 2 é igaul a '1'