'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima: MASTER'''

print("-="*25)
print("  Confederação Nacional  ")
print("-="*25)

ano = int(input("Digite o ano do seu nascimento: "))
idade = ano - 2024
if idade >= 9:
    print("CATEGORIA: MIRIM" )
elif (idade >= 9) and (idade < 14):
    print('CATEGORIA: INFANTIL')
elif (idade >= 14) and (idade < 19 ):
    print("CATEGORIA: JUNIOR")
elif (idade >= 19) and (idade >= 20) :  
    print("CATEGORIA: SENIOR")  
elif (idade < 20):
    print("CATEGORIA: MASTER")             