from src.data import storage

def test_storage_inicial(monkeypatch):
    monkeypatch.setattr(storage, "tareas", [])
    monkeypatch.setattr(storage, "contador_id", 1)
    assert storage.tareas == []
    assert storage.contador_id == 1

def test_storage_contador_incrementa(monkeypatch):
    monkeypatch.setattr(storage, "tareas", [])
    monkeypatch.setattr(storage, "contador_id", 1)
    storage.tareas.append({"id": storage.contador_id, "descripcion": "A"})
    storage.contador_id += 1
    assert storage.tareas[0]["id"] == 1
    assert storage.contador_id == 2
