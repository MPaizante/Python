
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
    print('{} convertendo apra Binario é igual a {}'.format(nb, bin(nb)))
elif op == 2:
    print('{} convertido para Octal é igual a {}'.format(nb , oct(nb)))
elif op == 3:
    print('{} convertido para Hexadecimal fica {}'.format(nb , hex(nb))) 
else:
    print('[ERRO] TENTE NOVAMENTE')