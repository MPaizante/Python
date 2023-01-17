p1 = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','merdao','programador','futuro')
for p in p1:
    print(f'\nNa palavra {p.upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')