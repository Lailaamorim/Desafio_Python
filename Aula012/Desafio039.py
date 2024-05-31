'''Faça um programa que leia o ano de nascimento de um jovem a informe, de acordo com sua idade:
- Sa ale ainda vai se alistar ao serviço militar.
- Sa é a hora de se alistar.
- Sa já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date

atual = date.today().year
# Obtém o ano atual usando a função today() da classe date

nasc = int(input("Ano de Nascimento: "))
idade = atual - nasc
# Calcula a idade subtraindo o ano de nascimento do ano atual

print(f"Quem nasceu em {nasc} tem {idade} anos em {atual}")

if idade == 18:
    print("Você tem que se alistar imediatamente!")
    # Se a idade for 18 anos, indica que o alistamento é imediato
elif idade < 18: 
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para o alistamento") 
    ano = atual + saldo
    print(f"Seu alistamento será em {ano}")
    # Se a idade for menor que 18 anos, calcula quantos anos faltam para o alistamento e em que ano ele ocorrerá
elif idade > 18 :
    saldo = idade -18
    print(f"Você já deveria ter se alistado há {saldo} anos.")    
    ano = atual - saldo 
    print(f"Seu alistamento foi em {ano}")
    # Se a idade for maior que 18 anos, calcula quantos anos se passaram desde o alistamento e em que ano ele ocorreu
