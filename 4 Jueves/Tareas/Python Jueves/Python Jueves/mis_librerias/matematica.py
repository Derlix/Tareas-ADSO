
def suma(num1, num2):
    """Suma de numeros"""
    return num1 + num2

def multiplicacion(num1,num2):
    return num1 * num2

def division(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error de division, el denominador no puede ser 0")


def guardarResultados(tipo_operacion, num1, num2, resultado):
    
    try:

        with open('C:/Users/arias/Desktop/resultados_matematica.txt','r') as archivo:
            mensaje = archivo.read()
            
        nuevo_mensaje = mensaje +"\n La " + tipo_operacion + " de: " + str(num1) + " con " + str(num2) + " es: " + str(resultado) 

        with open('C:/Users/arias/Desktop/resultados_matematica.txt','w2') as archivo:
            archivo.write(nuevo_mensaje)

    except:
        with open('C:/Users/arias/Desktop/resultados_matematica.txt','w') as archivo:
            mensaje = "\n La " + tipo_operacion + " de: " + str(num1) + " con " + str(num2) + " es: " + str(resultado)
            archivo.write(mensaje)