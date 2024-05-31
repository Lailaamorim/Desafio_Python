'''Desenvolva um programa que leia o primeiro termo e a razão de um a PA. No final, mostre os 10 primeiros 
termos dessa progressão'''

# Solicita ao usuário que insira o primeiro termo da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))

# Solicita ao usuário que insira a razão da PA
razao = int(input("Digite a razão da PA: "))

# Inicializa uma lista para armazenar os 10 primeiros termos da PA
termos = []

# Loop para calcular os 10 primeiros termos da PA
for i in range(10):
    # Calcula o i-ésimo termo da PA
    termo_atual = primeiro_termo + i * razao
    # Adiciona o termo atual à lista de termos
    termos.append(termo_atual)

# Exibe os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:", termos)
