from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title = 'Mi primer API 196',
    description = 'Emilio Márquez Morales',
    version='1.0.1'
) # Se instancia FastAPI

usuarios=[
    {"id":1, "nombre":"Emilio", "edad":20},
    {"id":2, "nombre":"Jos", "edad":22},
    {"id":3, "nombre":"Brayan", "edad":22},
]

@app.get('/',tags=["Inicio"]) # Se define la ruta

def main(): # Se define la función
    return {'hola FastAPI':'Emilio'}

@app.get('/promedio',tags=["Calificacion"])

def promedio():
    return('9') 

#endPoint Parametro obligatorio
@app.get('/usuario/{id}',tags=['Parametro obligatorio'])
def consultaUsuario(id:int):
    #conectaDB
    #Se realiza consulta y se retornan resultados
    return{"Se encontro el usuario":id}

#endPoint Parametro opcional
@app.get('/usuariox/',tags=["Parametro opcional"])
def consultaUsuario2(id:Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario['id'] == id:
                return {"mensaje":"Usuario encontrado","usuario":usuario}
        return{"mensaje":f"No se encontro el id: {id}"}
    else:
        return{"mensaje":"No se proporciono un ID"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
#Funcion asincrona: Si algo falla, se pasa a la siguiente función
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}

