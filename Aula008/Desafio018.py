# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

# Importa as funções 'radians', 'sin', 'cos' e 'tan' do módulo math
from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo que você deseja: "))
# Calcula o seno do ângulo convertendo-o para radianos com a função radians e usando a função sin
seno = sin(radians(angulo))
print(f"O ângulo de {angulo} tem o SENO de {seno}")

# Calcula o cosseno do ângulo convertendo-o para radianos com a função radians e usando a função cos
cosseno = cos(radians(angulo))
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno}")

# Calcula a tangente do ângulo convertendo-o para radianos com a função radians e usando a função tan
tangente = tan(radians(angulo))
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente}")

