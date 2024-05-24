#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input("Digite uma frase: ")
frase_maiuscula = frase.upper().strip()  # Armazena a frase em maiúsculas e sem espaços
frase_contagem = frase.find("A")# diz qual a primeira posiçaõ "A" apareceu pela primeira vez 
# se quiser que "A" apareça na posção 1 e não na zero é só colocar frase.find("A")+1
frase_ultima = frase.rfind("A")+1 #rfind significa procure apartir do lado direito 
print(f"Na frase a letra 'A' aparece {frase_maiuscula.count('A')} vezes")
print(f"A primeira letra A apareceu na posição: {frase_contagem}")
print(f"A última letra A apareceu na posição {frase_ultima}")