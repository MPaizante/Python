pessoas = {'nome' : 'Matheus', 'sexo' : 'M' , 'idade' : '23'}
pessoas['peso'] = 70
print (pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
Brasil = []   
estado = {'UF':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'UF':'São Paulo', 'sigla':'SP'}
Brasil.append(estado)
Brasil.append(estado2)

print(Brasil[0]['UF'])