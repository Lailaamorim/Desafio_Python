'''Cria uma tupla preenchida com os 20 primeiros colocados da Tabala do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados. B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética. D) Em que posição na tabela está o time da Chapecoense.'''

times = ('Botafogo', 'Flamengo', 'Bahia', 'São Paulo', 'Athletico-pr', 'Athlrtico-mg', 
'Red Bull Bragantino', 'Palmeiras', 'Internacional', 'Cruzeiro', 'Fortaleza', 'Juventude', 'Gremio',
'Vasco', 'Corinthians', 'Fluminense', 'Criciúma', 'Athético-Go', 'Cuiabá', 'Vitória')
print(f"Lista de Times Brasileirão: {times}")
print(f"A) 5 primeiros colocados: {times[0:5]}")
print(f"B) Últimos 4 colocados {times[-4:]}") #retorna os últimos 4 elementos da tupla times.
print(f"C) Ordem alfabética {sorted(times)}")
print(f"D) Time Criciúma está na {times.index('Criciúma')+1} posição")