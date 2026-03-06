import pytest
from src.data import storage

def test_storage_inicial():
    storage.tareas.clear()
    storage.contador_id = 1
    assert storage.tareas == []
    assert storage.contador_id == 1