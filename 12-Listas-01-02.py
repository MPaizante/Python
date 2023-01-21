g = [['J' , 19] , ['A' , 33] , ['Jo', 13] , ['Maria' , 45]]
for p in g:
    print(p)
    print(f'{p[0]} tem {p[1]} anos de idade.  ')
    
gal = list()
d = list()
for c in range(0,3):
    d.append(str(input('Nome:')))
    d.append(int(input('Idade:')))
    gal.append(d[:])
    
print(gal)
