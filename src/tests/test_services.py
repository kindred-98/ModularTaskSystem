import pytest
from src.services import tareas_service
from src.data import storage

@pytest.fixture(autouse=True)
def limpiar_storage():
    storage.tareas.clear()
    storage.contador_id = 1

def test_agregar_tarea_valida():
    ok, msg = tareas_service.agregar_tarea("Comprar leche")
    assert ok
    assert "✅ Tarea #1 añadida" in msg
    assert len(storage.tareas) == 1

def test_completar_tarea_existente():
    tareas_service.agregar_tarea("Estudiar Python")
    ok, msg = tareas_service.completar_tarea("1")
    assert ok
    assert storage.tareas[0]["completada"]

def test_eliminar_tarea_existente():
    tareas_service.agregar_tarea("Hacer ejercicio")
    ok, msg = tareas_service.eliminar_tarea("1")
    assert ok
    assert len(storage.tareas) == 0