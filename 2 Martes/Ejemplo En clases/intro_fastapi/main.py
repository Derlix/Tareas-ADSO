from fastapi import FastAPI

app = FastAPI()

@app.get("/") #Objet creado  GET es un metodo 
def read_root():
    return {"Hello": "World"}

@app.get('/saludar/')
def saludar():
    return {"Mensaje":"Hola ADSO 2670586"}

@app.get('/sumar/')
def sumar_dos_numeros():
    n1 = 30
    n2 = 40
    suma = n1 + n2 

    datos = {
        "numero":n1,
        "numero2":n2,
        "Resultado":suma
        }
    return datos

@app.get('/operaciones/')
def sumar_dos_numeros():
    n1 = 30
    n2 = 10
    suma = n1 + n2 
    resta = n1 -n2
    multiplicacion = n1 * n2
    if n1 == 0 or n2==0:
        division = "Division no disponible"
    else:
        division = n1 / n2
    datos = {
        "numero":n1,
        "numero2":n2,
        "Suma":suma,
        "Resta":resta,
        "Multiplicacion":multiplicacion,
        "Division":division
        }
    return datos