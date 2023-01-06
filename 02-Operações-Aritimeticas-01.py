#print ('Matheus é {:20}') isso vai fazer da vinte espaços, se eu botar :>20 a variavel vai andar para a direita e :<20 vai andar para esquerda, :^20 vai centrarlizar e se botar :=^20 vai criar 20= com a variavel centralizada.
n1 = float(input('Numero:'))
n2 = float(input('Numero:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print ('A soma vale {} multiplicação vale {} divisão vale {}! '.format(s , m , d) , end ='')
print('Divisão inteira {} e potencia {}! '.format(di , e)) #\n (quebra a linha)

m1 = int(input('valor:'))
dobro = m1*2
triplo = m1*3
raiz = m1**0.5

print('Dobro {} triplo {} raiz {}!'.format(dobro , triplo , raiz))

Nome = input('Seu nome:')
Nota1 = int(input('valor:'))
Nota2 = int(input('valor:'))
Media = (Nota1+Nota2)/2
print('O aluno {} tirou as seguintes notas, primeira nota foi {} a segunda nota foi {} a sua media foi {}! '.format(Nome , Nota1 , Nota2 , Media))

#Antecessor e sucessor
bora = int(input('Digite um numero:'))
ant = bora-1
suc = bora +1
print('O sucessor de {} é {} e seu antecessor é {}. '.format(bora , suc, ant))
