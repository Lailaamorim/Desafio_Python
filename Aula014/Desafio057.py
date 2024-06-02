#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado
#peça a digitação novamente até ter um valor correto.

while True:
    sexo=input("Insrira o sexo da pessoa: [M/F] ").strip.upper()
    if sexo == 'M'or sexo == 'F':
        print("Sexo inserido com sucesso!")
        break
    else:
        print("Opção inválida, tente novamente!")    