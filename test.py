jog = dict()
partidas = list()
jog ['nome'] = str(input('Nome do Jogador:'))
tot = int(input(f'Quantas partidas {jog["nome"]} jogou?'))
for ct in range(0 , tot):
    partidas.append(int(input(f'    Quantos gols na partida {ct+1}?   ')))
jog['gols'] = partidas[:]
jog['total'] = sum(partidas)
for ke , vt in jog.items():
    print(f'O campo {ke} tem o valor {vt} ')
print(jog)
print(partidas)                   
print(f'O jogador {jog["nome"]} jogouj {len(jog["gols"])} partidas. ')
for iii , vvv in enumerate(jog['gols']):
    print(f'             => Na partida {iii}, fez {vvv} gols.  ')
print(f'Foi um total de {jog["total"]} gols. ')
