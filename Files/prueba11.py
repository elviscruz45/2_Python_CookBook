
lista=[1,2,3,4,5,6]
casa=[x**2 for x in lista]
cuarto=(x**2 for x in lista)

print(next(cuarto))
print(next(cuarto))
print(next(cuarto))