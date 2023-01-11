from datetime import date
#Aprovando Emprestimo
vc = float(input('QUal valor da casa?'))
Salvc = float(input('Qual salario do comprador?'))
Avc = float(input('Quantos anos vc quer pagar?'))
pres = vc/(Avc * 12)
Salm = (Salvc *30) / 100
print('Para pagar um casa de {:.2f} em {} anos a prestação será de {:.2f}.'.format(vc , Avc , pres))
if pres < Salm:
    print('Aprovado')
else:
    print('Negado.')
    
    
#conversor de bases numericas
nb = int(input('Digite um numero inteiro:'))
print('''Escolha a base de conversão:
[1] Binario
[2] Octal
[3] Hexadecimal  ''')
op = int(input('Sua opção:'))
if op == 1:
    print('{} convertendo apra Binario é igual a {}'.format(nb, bin(nb)[2:]))
elif op == 2:
    print('{} convertido para Octal é igual a {}'.format(nb , oct(nb)[2:]))
elif op == 3:
    print('{} convertido para Hexadecimal fica {}'.format(nb , hex(nb)[2:])) 
else:
    print('[ERRO] TENTE NOVAMENTE')
    
#comparando numeros
nc1 = int(input('Digite um numero:'))
nc2 =  int(input('Digite um numero:'))
if nc1 > nc2:
    print('primeiro é maior')
elif nc1 == nc2:
    print('Iguais')
else:
    print('Segundo é maior')    
    

#Alistamento militar
AnoAtual = date.today().year
AnoNas =int(input('Ano de anscimento:'))
AnoIdade = AnoAtual - AnoNas
print('Quem nasceu em {} tem idade de {} ano em {}.'.format(AnoNas , AnoIdade , AnoAtual))
if AnoIdade >= 18:
    print('Tem que se alistar')
elif AnoIdade == 18:
    print('Se alista')
else:
    print('Ainda n precisa se alistar.')