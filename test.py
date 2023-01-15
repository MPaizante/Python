n = 0
s = 0
contador = 0
while True:
    n = int(input('Leia:'))
    if n == 999:
        break
    contador += 1
    s += n
print(f'A soma é {s} a quantidade de vezes foi {contador}.')



