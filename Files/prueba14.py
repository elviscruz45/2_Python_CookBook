def funcion_generadora_prints():
    print("GENERADOR: Se va a generar un PRIMER dato")
    yield "valorGenerado1"

    print("GENERADOR: Se va a generar un SEGUNDO dato")
    yield "valorGenerado2"

    print("GENERADOR: Se va a generar un TERCER dato")
    yield "valorGenerado3"

    print("GENERADOR: Termina y lanzará automáticamente la excepción StopIteration")
    
    

def funcion_generadora_prints():
    # …

    print("GENERADOR: Termina y lanzará automáticamente la excepción StopIteration")

    return
    # El return void en una “función Generadora” lanza un raise StopIteration