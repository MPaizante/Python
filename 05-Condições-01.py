tempo = int(input('Tempo:'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
    print('fim')
    
#elogio a indentação importa

n = str(input('Qual seu nome?'))
if n  == 'Matheus':
    print('Que nome lindo!')
else:
    print('legal')
    
#Media
n1 = float(input('Digite a nota:'))
n2 = float(input('Digite a nota:'))
m = (n1 + n2)/2
print('A media foi {}'.format(m))
if m >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')