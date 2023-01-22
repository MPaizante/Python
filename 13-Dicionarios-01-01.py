from random import randint
from time import sleep
from operator import itemgetter
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



