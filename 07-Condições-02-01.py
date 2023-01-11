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
    


#Nota Media
nt1 = float(input('Digite a nota:'))
nt2 = float(input('Digite a nota:'))
ntg = (nt1 + nt2)/2
if 10 >= ntg > 7:
    print('Aprovado')
elif 7 > ntg > 5:
    print('Recuperação')
elif ntg < 4.9:
    print('Reprovado')
else:
    print('Erro')


    
#Classificação de Atletas categorias
nata1 = date.today().year
nata2 = int(input('Ano de nascimento:'))
nata3 = nata1 - nata2
print('O atleta tem {} anos.'.format(nata3))
if nata3 <= 9:
    print('Mirim')
elif nata3 > 9 and nata3 <=14:
    print('Infantil')
elif  nata3 <= 19:
    print('Junior')
elif nata3 <= 25:
    print('Senior')
elif nata3 <= 60:
    print('Adulto')
else:
    print('Idoso')  
    
    
#Analisando triangulos
rt1 = float(input('Digite um valor:'))
rt2 = float(input('Digite um valor:'))
rt3 = float(input('Digite um valor:'))
if rt1 < rt2+rt3 and rt2 < rt1 +rt3 and rt3 < rt1 + rt2:
    print('Pode ser um triangulo.')
    if rt1 == rt2 == rt3:
        print('Equilatero')
    elif rt1 != rt2 != rt3 != rt1:
        print('Escaleno')
    else:
        print('Isoceles') 
else:
    print('N pode ser um triangulo.')
    
    
#IMC
p12 = float(input('Digite o peso:'))
a12 = float(input('Digite a altura em metros: '))
imc = p12/(a12**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Ta normal filhao!')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30<= imc < 40:
    print('Obeso')
elif imc >= 40:
    print('cuidado')
