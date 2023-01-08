frase = 'Curso em Video Python'
print()
print(frase[:14])
print(frase.count('o'))
print(len(frase.strip()))
print('Curso' in frase)
print(frase.split())

print("""O conto é um tipo de história literária. Geralmente, é uma obra de ficção, ou 
      seja, de faz de conta, pois retrata um mundo de fantasia a partir da imaginação de quem
      o escreveu. O conto tem narrador e um enredo, isto é, uma história que vai se desenvolver com começo, meio e fim.""")

#analizador te texto
nome = str(input('Digite um nome:')).strip()
print('Nome maiusculo: {}'.format(nome.upper()))
print('Nome em minusculo: {}'.format(nome.lower()))
print('Sem contar o espaços {}'.format(len(nome) - nome.count(' ')))
print(nome.find(' '))

#Separando digitos de um numero
numi = int(input('Numero:'))
nums= str(numi)
peleu = numi // 1 % 10
peled = numi // 10 % 10
pelec = numi // 100 % 10
pelem = numi // 1000 % 10
print('Analisando um numero {}.'.format(numi))
print('Unidade: {}'.format(nums[3]))
print('Dezena: {}'.format(nums[2]))
print('Centena: {}'.format(nums[1]))
print('Milhar: {}'.format(nums[0]))
#ou pode fazer assim
print('Analisando um numero {}.'.format(numi))
print('Unidade: {}'.format(peleu))
print('Dezena: {}'.format(peled))
print('Centena: {}'.format(pelec))
print('Milhar: {}'.format(pelem))

#Verificador de letra

cidade = str(input('Em que cidade vc nasceu:')).strip()
print(cidade[0:5].upper() == 'Santo') #n importa se escrever maiusculo ou minusculo, o upper vai jogar oque escrever para maiusculo


#String dentro de String
nomect = str(input('Qual nome:')).strip()
print('Seu nome tem silva? {}'.format('silva' in nomect.lower()))


#Primeira e ultima letra
frase1 = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase1.count('A')))
print('A primeiro letra A apareceu na posição {}'.format(frase1.find('A')+1))
print('A ultima letra apareceu na posição {}.'.format(frase.rfind('A')+1))

#Primeiro e ultimo nome
bmx = str(input('fala o nome cachorra:')).strip()
bmxn = bmx.split()
print('Seu primeiro nome é {}.'.format(bmxn[0]))
print('Seu ultimo nome é {}'.format(bmxn[len(bmxn)-1]))


