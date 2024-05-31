'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de 
um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER'''

from datetime import date

atual = date.today().year
# Obtém o ano atual usando a função today() da classe date

print("-="*25)
print("  Confederação Nacional  ")
print("-="*25)

nascimento = int(input("Digite o ano do seu nascimento: "))
# Solicita ao usuário que insira o ano de nascimento e converte a entrada para um valor inteiro

idade = atual - nascimento
# Calcula a idade subtraindo o ano de nascimento do ano atual

if idade <= 9:
    print("CATEGORIA: MIRIM" )
    # Se a idade for menor ou igual a 9 anos, exibe a categoria como Mirim
elif idade <= 14:
    print('CATEGORIA: INFANTIL')
    # Se a idade estiver entre 10 e 14 anos, exibe a categoria como Infantil
elif idade <= 19:
    print("CATEGORIA: JUNIOR")
    # Se a idade estiver entre 15 e 19 anos, exibe a categoria como Júnior
elif idade <= 25:  
    print("CATEGORIA: SENIOR")  
    # Se a idade estiver entre 20 e 25 anos, exibe a categoria como Sênior
else:
    print("CATEGORIA: MASTER")
    # Se a idade for superior a 25 anos, exibe a categoria como Master
