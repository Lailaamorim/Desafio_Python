# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
#calcule e mostre o comprimento da hipotenusa

#MANEIRA MATEMATICA

#co = float(input("Comprimento do cateto oposto: "))
#ca = float(input("Comprimento do cateto adjacente: "))
##print(f"A hipotenusa vai medir {hi:.2f}")

#MANEIRA COM IMPORTAÇÃO
# Importa o módulo math, que contém funções matemáticas
import math

# Solicita ao usuário que insira o comprimento do cateto oposto e do cateto adjacente, convertendo as entradas para valores float
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))

# Calcula a hipotenusa usando o teorema de Pitágoras com a função hypot do módulo math
hi = math.hypot(co, ca)

# Exibe o valor da hipotenusa com duas casas decimais
print(f"A hipotenusa vai medir {hi:.2f}")

