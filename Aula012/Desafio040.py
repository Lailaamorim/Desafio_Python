'''Crie um programa que leia duas notas de um aluno a calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
Média entre 5.0 a 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

cores = {
    'para':  '\033[m',
    'red':   '\033[4;31;40m',
    'blue':  '\033[4;34;40m',
    'green': '\033[4;32;40m'
}

media = (nota1 + nota2) / 2

if media < 5.0 :
    print(f"{cores['red']}REPROVADO!{cores['para']}😭")
elif 5.0 <= media <= 6.9:
    print(f"{cores['blue']}RECUPARAÇÃO!{cores['para']}😬😬")
elif media >= 7.0:
    print(f"{cores['green']}APROVADO!😍{cores['para']}")    
    
'''
A condição 5.0 <= media <= 6.9 significa que a variável media deve ser maior ou igual 
a 5.0 e menor ou igual a 6.9.

O operador <= significa "menor ou igual a".
O operador >= significa "maior ou igual a".'''

