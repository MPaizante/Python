from datetime import date
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
   