'''Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de 
triângulo será formado:

- Equilátero: todos os lados iguais - Isóscales: dois lados iguais

-Escalano: todos os lados diferentes'''

print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)

r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float (input("Teceiro Segmento: "))
# Verificar se os lados formam um triângulo
if r1 + r2  <=  r3 or r1 + r3 <= r2 or r2 + r3 <= r1:
    print("Os lados não formam um triângulo")
    print("O Triângulo é escaleno.")  
elif r1 == r2 or r2 == r3 or r1 == r3:   # Classificar o triângulo 
    print("O Triângulo é Isósceles.")
else: 
    print("O Triângulo é escaleno.")   