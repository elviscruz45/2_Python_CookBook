from tkinter import *

raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()
operacion=""
resultado=0
#----------------------Pantalla--------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=40)
pantalla.config(background="black",fg="#03f943",justify="right")

#------------------------Pulsaciones Teclado--------------------------
def numeroPulsado(num):
    global operacion
    a=numeroPantalla.get()
    if a:
        a=int(a)
        a=str(a)
    if a=="0":
        a=""
    b=a+num
    
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(b)

#------------------------Funcion suma--------------------------
def suma(num):
    global operacion
    global resultado
    operacion="suma"
    resultado+=int(num)
    numeroPantalla.set(resultado)

#------------------------Funcion el resultado--------------------------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado=0

#------------------------Fila 2--------------------------
boton7=Button(miFrame,text="7",width=2,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=2,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=2,command=lambda:numeroPulsado('9'))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=2)
botonDiv.grid(row=2,column=4)
#------------------------Fila 3--------------------------

boton4=Button(miFrame,text="4",width=2,command=lambda:numeroPulsado('4'))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=2,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=2,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="x",width=2)
botonMult.grid(row=3,column=4)

#------------------------Fila 4--------------------------
boton7=Button(miFrame,text="1",width=2,command=lambda:numeroPulsado("1"))
boton7.grid(row=4,column=1)
boton8=Button(miFrame,text="2",width=2,command=lambda:numeroPulsado("2"))
boton8.grid(row=4,column=2)
boton9=Button(miFrame,text="3",width=2,command=lambda:numeroPulsado("3"))
boton9.grid(row=4,column=3)
botonRest=Button(miFrame,text="-",width=2)
botonRest.grid(row=4,column=4)

#------------------------Fila 5--------------------------
boton0=Button(miFrame,text="0",width=2,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",",width=2,command=lambda:numeroPulsado(","))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=2,command=lambda:el_resultado())
botonIgual.grid(row=5,column=3)
botonSum=Button(miFrame,text="+",width=2,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5,column=4)










raiz.mainloop()