'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER'''

from datetime import date
atual = date.today().year

print("-="*25)
print("  Confederação Nacional  ")
print("-="*25)

nascimento = int(input("Digite o ano do seu nascimento: "))
idade = atual - nascimento 
if idade <= 9:
    print("CATEGORIA: MIRIM" )
elif (idade <= 14):
    print('CATEGORIA: INFANTIL')
elif (idade <= 19 ):
    print("CATEGORIA: JUNIOR")
elif (idade <= 25) :  
    print("CATEGORIA: SENIOR")  
else:
    print("CATEGORIA: MASTER")             