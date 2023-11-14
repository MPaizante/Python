carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Golf", "Focus", "Onyx", "Fit"]

itCarros = iter(carros)


#print(next(itCarros))
#print(next(itCarros))
#print(next(itCarros))
#print(next(itCarros))
#print(next(itCarros))


while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break

"""i = 0
x = len(carros)
while i < x:
    print(carros[i])
    i+=1"""