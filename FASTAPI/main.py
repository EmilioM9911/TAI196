from fastapi import FastAPI, HTTPException
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
    {"id":4, "nombre":"Toñito", "edad":21},
]

@app.get('/',tags=["Inicio"]) # Se define la ruta

def main(): # Se define la función
    return {'hola FastAPI':'Emilio'}

#endpoint Consultar todos los usuarios
@app.get('/usuarios',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return {"Usuarios Registrados ": usuarios}

#endpoint para agregar usuarios
@app.post('/usuario/',tags=['Operaciones CRUD'])
def AgregarUsuario(usuarionuevo: dict):
    for usr in usuarios:
        if usr["id"] == usuarionuevo.get("id"):
            raise HTTPException(status_code= 400, detail="Usuario existente")
    
    usuarios.append(usuarionuevo)
    return usuarionuevo 

#endpoint para actualizar usuario
@app.put('/usuario/{id}',tags=["Operaciones CRUD"])
def ActualizarUsuario(id:int, usuarioactualizado:dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuarioactualizado)
            return("Usuario actualizado")
    raise HTTPException(status_code= 400, detail="Usuario no encontrado")
    

#endpoint para eliminar usuario
@app.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    for i in range(len(usuarios)):
        if usuarios[i]["id"]==id:
            usuarios.pop(i)
            return {"mensaje":"usuario eliminado"}
    raise HTTPException(status_code=404,detail="usuario no encontrado")

    