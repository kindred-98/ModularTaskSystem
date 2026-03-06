"""
validators.py

Funciones de validación de entradas del usuario.
"""

def validar_descripcion(descripcion: str):
    descripcion = descripcion.strip()
    if len(descripcion) < 3:
        return False, "La tarea debe tener al menos 3 caracteres."
    return True, descripcion

def validar_id(valor: str):
    try:
        id_ = int(valor)
        if id_ <= 0:
            raise ValueError
        return True, id_
    except ValueError:
        return False, "El ID debe ser un número entero positivo."