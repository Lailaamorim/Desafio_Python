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
# Define códigos de cores ANSI para uso na formatação do texto

media = (nota1 + nota2) / 2
# Calcula a média das duas notas

if media < 5.0:
    print(f"{cores['red']}REPROVADO!{cores['para']}😭")
    # Se a média for menor que 5.0, exibe uma mensagem de reprovação em vermelho
elif 5.0 <= media <= 6.9:
    print(f"{cores['blue']}RECUPERAÇÃO!{cores['para']}😬😬")
    # Se a média estiver entre 5.0 e 6.9, exibe uma mensagem de recuperação em azul
elif media >= 7.0:
    print(f"{cores['green']}APROVADO!😍{cores['para']}")
    # Se a média for 7.0 ou superior, exibe uma mensagem de aprovação em verde   
    
'''
A condição 5.0 <= media <= 6.9 significa que a variável media deve ser maior ou igual 
a 5.0 e menor ou igual a 6.9.

O operador <= significa "menor ou igual a".
O operador >= significa "maior ou igual a".'''

