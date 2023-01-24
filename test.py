def leiaInt(msg):
    ok = False
    v1 = 0
    while True:
        n1 = str(input(msg))
        if n1.isnumeric():
            v1 = int(n1)
            ok = True
        else:
            print('\033[0;31mErro! Digite novamente.\033[m')
        if ok:
            break
    return v1


n1 = leiaInt('Digite um numero:')
print(f'Voce acabou de digitar o numero {n1}')