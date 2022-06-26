#Funcion map
class empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}Dolar".format(self.nombre,self.cargo,self.salario)
    

lista_empleados=[
    empleado("Juan","director",75),
    empleado("Ana","presidente",15),
    empleado("antonio","administrativo",25),
    empleado("sara","secretaria",35),
    empleado("Mario","Botones",45),
]

'''
def calculo_comision(empleado):
    empleado.salario=empleado.salario*1.03
    return empleado
'''


