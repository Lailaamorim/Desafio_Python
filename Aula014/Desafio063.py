#Escreva um programa que leia um número n inteiro qualquer a mostre na tela os n primeiros elementos de uma 
#Sequência de Fibonacci.

#Ex:

#0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 

print("-" * 30)
print("Sequência de Fibonacci")
print("-" * 30)

n = int(input("Quantos Termos você quer mostrar? "))

# Inicializa os dois primeiros termos da sequência de Fibonacci
t1 = 0  # Primeiro termo da sequência
t2 = 1  # Segundo termo da sequência

print("~" * 30)  # Exibe uma linha de 30 caracteres '~' para decoração
print(f"{t1} → {t2}", end='')  # Exibe os dois primeiros termos da sequência, seguidos de uma seta

cont = 3 # Inicializa o contador com 3, pois os dois primeiros termos já foram exibidos


# Loop para gerar e exibir os termos da sequência de Fibonacci até o n-ésimo termo
while cont <= n:
    t3 = t1 + t2  # Calcula o próximo termo da sequência somando os dois termos anteriores
    print(f" → {t3}", end='')  # Exibe o próximo termo, seguido de uma seta
    t1 = t2  # Atualiza o valor de t1 para o próximo cálculo
    t2 = t3  # Atualiza o valor de t2 para o próximo cálculo
    cont += 1  # Incrementa o contador

print(' → FIM')  # Exibe "FIM" após o término da sequência