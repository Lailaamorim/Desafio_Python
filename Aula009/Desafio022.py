# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras tem ao todo (sem considerar os espaços) 
# Quantas letras tem o primeiro nome

import time


nome = input("Digite seu nome: "). strip()# Elimina espaços em branco antes e depois do nome
print("   Analisando seu nome...")
time.sleep(1)  # Simula um atraso de um segundo

print(f"Seu nome em maiúscula é: {nome.upper()}")  # .upper converte para letras maiúsculas
print(f"Seu nome em minúsculo é: {nome.lower()}")  # .lower converte para letras minúsculas
print(f"Seu nome tem ao todo: {len(nome) - nome.count(' ')} letras")  # Conta letras excluindo espaços
# -nome.count(' ') ele elimina os espaços entre as palavras
print(f"Seu primeiro nome tem {nome.find(' ')} caractere")# encontra o primeiro espaço do primeiro nome