from random import randint
from time import sleep
from operator import itemgetter
from datetime import datetime
pessoas = {'nome' : 'Matheus', 'sexo' : 'M' , 'idade' : '23'}
pessoas['peso'] = 70
print (pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
Brasil = []   
estado = {'UF':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'UF':'São Paulo', 'sigla':'SP'}
Brasil.append(estado)
Brasil.append(estado2)

print(Brasil[0]['UF'])

estado58 = dict()
brasil6 = list()
for c in range(0,3):
    estado58['uf'] = str(input('Unidade Federativa: '))
    estado58['sigla'] = str(input('Sigla do Estado: '))
    brasil6.append(estado58.copy())
for e in brasil6:
    print(e)
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}.')    
print(brasil6)


#Dicionario em Python
aluno = dict()
aluno['nome'] = str(input('Nome do Aluno:'))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >=7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno ['situação'] = 'Recuperção'
else:
    aluno['situação'] = 'Reprovado'
for ch , va in aluno.items():
    print(f' -{ch} é igual a {va}')


#Jogo de Dados em Python
jogo1 = {   'jogador1': randint(1 , 6),
            'jogador2': randint(1 , 6),
            'jogador3': randint(1 , 6),
            'jogador4': randint(1 , 6)
}
print(jogo1)
print('Valores sorteados:')
for ke , vi in jogo1.items():
    print(f'{ke} tirou {vi} no dado.')
    sleep(1)
ranking = sorted(jogo1.items(), key=itemgetter(1), reverse=True )
print(ranking)
print('Ranking dos jogadores.')
for ii , vi in enumerate(ranking):
    print(f'{ii+1}º lugar: {vi[0]} com {v[1]}.')


#Cadastro de trabalhador em Python
dados = dict()
dados['nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento:'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação:'))
    dados['salario'] = float(input('Salario:'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for t , w in dados.items():
    print(f'  -{t} tem o valor {w}')
    
#Cadastro de Jogador de Futebol
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


#Unindo Dicionario e lista.
p = dict()
galera = list()
soma5 = media5 = 0
while True:
    p['nome'] = str(input('Nome:'))
    while True:
        p['sexo'] = str(input('Sexo:')).upper()[0]
        if p['sexo'] in 'MF':
            break
        print('ERRO')
    p['idade'] = int(input('Idade:'))
    soma5 += p['idade']
    galera.append(p.copy())
    while True:
        r = str(input('Quer continuar?')).upper()[0]
        if r in 'SN':
            break
        print('Erro!')
    if r == 'S':
        break
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
media5= soma5 / len(galera)
print(f'A media das idade é de {media5:5.2f} anos. ')
print(f'As mulheres cadastradas foram' , end=' ')
for ppp in galera:
    if ppp['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=' ')
print()
print('Lista das pessaos acima da media:', end='')
if ppp in galera:
    if ppp['idade'] >= media5:
        print('        ')
        for kkkk , vvvvv in ppp.items():
            print(f'{kkkk} = {vvvvv} ', end=' ')
            print()
print('<< Encerrado >>')

#Aprimorando Dicionarios













