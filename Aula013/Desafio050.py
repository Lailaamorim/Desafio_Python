'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere- o.'''

# Inicializa a variável soma como zero
soma = 0
cont = 0
for numero in range(1, 7):# Loop que itera de 1 a 6 (inclusive)
    # Solicita ao usuário que insira um número e o converte para inteiro
    n = int(input("Insira um número: "))
    # Verifica se o número inserido é par
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
# Após o loop, imprime a soma dos números pares
print(f"Você informaou {cont} números Pares, A soma dos números pares é {soma}")
