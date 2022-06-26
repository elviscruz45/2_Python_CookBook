# Funcion Lambda
area_triangulo=lambda x,y:x*y/2

area_triangulo(2,3)

# Funcion Filter

numeros=[17,24,7,39,8,51,92]

print(list(filter(lambda numeros:numeros%2==0,numeros)))