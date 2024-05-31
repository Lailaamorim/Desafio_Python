'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto'''
from datetime import date
# Importa a classe 'date' do módulo datetime, que permite trabalhar com datas

ano = int(input("Que ano você quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
    # Se o usuário inserir 0, o ano atual é obtido usando a função today() da classe 'date'

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # Verifica se o ano é divisível por 4, mas não por 100, ou se é divisível por 400 (condições para ser bissexto)
    print(f"O ano {ano} é BISSEXTO")
    # Se o ano atender às condições, imprime uma mensagem informando que é bissexto
else:
    print(f"O ano {ano} NÃO É BISSEXTO")
    # Se o ano não atender às condições, imprime uma mensagem informando que não é bissexto

