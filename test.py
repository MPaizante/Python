ficha = list()
while True:
    nome6 = str(input('Nome:'))
    nota5 = float(input('Nota1:'))
    nota4 = float(input('Nota2:'))
    media = (nota4 + nota5) / 2
    ficha.append([nome6 , [nota4 , nota5] , media])
    re = str(input('Quer continuar ? [S/N]: ')).strip().upper()
    if re in 'N':
        break
print(f'{"No.":<4}{"NOME6":<10}{"MEDIA":>8}')
for i , a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opc == 999:
        print('Finalizado')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]}')
print('Volte sempre.')