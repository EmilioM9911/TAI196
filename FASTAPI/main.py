from fastapi import FastAPI

app = FastAPI() # Se instancia FastAPI

@app.get('/') # Se define la ruta

def main(): # Se define la función
    return {'hola FastAPI':'Emilio'}


