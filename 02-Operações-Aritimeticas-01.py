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

#dobro
m1 = int(input('valor:'))
dobro = m1*2
triplo = m1*3
raiz = m1**0.5
print('Dobro {} triplo {} raiz {}!'.format(dobro , triplo , raiz))

#media do aluno
Nome = input('Seu nome:')
Nota1 = float(input('valor:'))
Nota2 = float(input('valor:'))
Media = (Nota1+Nota2)/2
print('O aluno {} tirou as seguintes notas, primeira nota foi {:.1f} a segunda nota foi {:.1f} a sua media foi {:.1f}! '.format(Nome , Nota1 , Nota2 , Media))

#Antecessor e sucessor
bora = int(input('Digite um numero:'))
ant = bora-1
suc = bora +1
print('O sucessor de {} é {} e seu antecessor é {}. '.format(bora , suc, ant))

#conversor
con = float(input('Distancia em metros:'))
cm = con * 100
mm = con * 1000
print('A medida de {}m corresponde a {}cm e {}mm . '.format(con , cm , mm))

#tabuada
ni = int(input('Digite um numero para ver a tabuada:'))
print('{} x {} = {}  '.format(ni , 0 , ni*0))
print('{} x {} = {}  '.format(ni , 1 , ni*1))
print('{} x {} = {}  '.format(ni , 2 , ni*2))
print('{} x {} = {}  '.format(ni , 3 , ni*3))
print('{} x {} = {}  '.format(ni , 4 , ni*4))
print('{} x {} = {}  '.format(ni , 5 , ni*5))
print('{} x {} = {}  '.format(ni , 6 , ni*6))
print('{} x {} = {}  '.format(ni , 7 , ni*7))
print('{} x {} = {}  '.format(ni , 8 , ni*8))
print('{} x {} = {}  '.format(ni , 9 , ni*9))
print('{} x {} = {}  '.format(ni , 10 , ni*10))
