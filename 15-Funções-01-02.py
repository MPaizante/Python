#Função para votação
from datetime import date
def voto(ano):
    atual = date.today().year  
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos não vota.  '
    elif 16 <= idade <= 18 or idade > 65:
        return f'Voto opcional'
    else:
        return f'Com {idade} anos o voto é obrigatorio'


print(voto(2000))
mes = date.today().month 