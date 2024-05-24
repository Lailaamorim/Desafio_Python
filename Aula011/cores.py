'''Cores no Terminal 

ANSI 
escape seguence { Para o terminal}
Sempre que vc quiser representar uma cor em python, você vai começar com \033[m   Entre esse "colchete" e "M"
você vai colocar o codigo da cor 
Ex:

\033[ style ; text ; back m

Style = Codigo do comportamento, estilo da fonte
text = Codigo do texto // cor dp texto
back = Codigo do background = Cor de fundo 

style

0 = none : sem estilo nenhum
1 = bold : Coloca em negrito
4 = underline
7 = inverte as configurações // o que colocou para fundo vai para letra e virse-versa

text 

cores do texto
30 = branco
31 = vermelho
32 = verde
33 = amarelo
34 = azul
35 = lilas
36 = ciano
37 =  cinza

back 

a back tem as mesas cores do texto que vão do 40 ao 47 
'''
print("\033[1;31;43mOlá, Mundo!\033[m")
print("\033[4;34;46mOlá, Mundo!\033[m")
print("\033[0;30;41mOlá, Mundo!\033[m")
print("\033[4;33;41mOlá, Mundo!\033[m")
print("\033[1;35;43mOlá, Mundo!\033[m")
print("\033[30;42mOlá, Mundo!\033[m")
print("\033[33mOlá, Mundo!\033[m")
print("\033[7;30mOlá, Mundo!")

a = 3
b = 5
print(f"Os valores são \033[32;41m{a}\33[m e \033[31;42m{b}\033[m!!!")

nome  = "Laila"
cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco': '\033[7;30m'
}

print(f"Olá! Muito prazer em te conhecer,{cores['azul']}{nome}{cores['limpa']}  ")
print(f"Olá! Muito prazer em te conhecer,{cores['amarelo']}{nome}{cores['limpa']}")
print(f"Olá! Muito prazer em te conhecer,{cores['pretoebranco']}{nome}{cores['limpa']}")

