# a simple file writer object

class MessageWriter:
    def __init__(self,hola):
        self.hola=hola
        
        

a=MessageWriter("casa")
b=MessageWriter("casa")

print(id(a))
print(id(b))


