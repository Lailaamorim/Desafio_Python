'''Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços
ex: apos a sopa 
a sacada da casa
a torre da derrota
o lobo ama o bolo'''

frase = input("Digite uma frase: ")

#remover espaços e conerter para minúsculas 
frase_limpa = ''.join(frase.split()).lower()

#Verifica se a frase é igual à sua inversa
if frase_limpa == frase_limpa[::-1]:
    print(f"A fase {frase} é um palíndromo: {frase_limpa}")
else:
    print(f'A frase {frase} não é um palíndromo.')    

'''Remover Espaços e Converter para Minúsculas:
frase.split(): Divide a frase em uma lista de palavras. Por exemplo, se a entrada for "A sacada da casa", 
split() retorna a lista ['A', 'sacada', 'da', 'casa'].

''.join(frase.split()): Junta as palavras da lista novamente em uma única string, sem espaços. 
Usando o exemplo anterior, 'A', 'sacada', 'da', 'casa' se transforma em 'Asacadadacasa'.

.lower(): Converte todos os caracteres para minúsculas. Então 'Asacadadacasa' se transforma em 'asacadadacasa'.
O resultado final é uma string sem espaços e em letras minúsculas, armazenada em frase_limpa.

Verificar se é um Palíndromo:

frase_limpa == frase_limpa[::-1]: Compara frase_limpa com sua versão invertida.
frase_limpa[::-1]: Utiliza slicing para criar uma string que é a inversa de frase_limpa. 
Por exemplo, se frase_limpa for 'asacadadacasa', frase_limpa[::-1] será 'asacadadacasa'.
Se frase_limpa é igual a frase_limpa[::-1], a frase é um palíndromo.
if frase_limpa == frase_limpa[::-1]: Se a condição for verdadeira, significa que a frase é um palíndromo.
'''