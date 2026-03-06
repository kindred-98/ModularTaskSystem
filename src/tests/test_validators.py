import pytest
from src.utils.validators import validar_descripcion, validar_id

def test_validar_descripcion_valida():
    ok, resultado = validar_descripcion("Comprar leche")
    assert ok
    assert resultado == "Comprar leche"

def test_validar_descripcion_corta():
    ok, mensaje = validar_descripcion("a")
    assert not ok
    assert mensaje == "La tarea debe tener al menos 3 caracteres."

def test_validar_id_valido():
    ok, resultado = validar_id("5")
    assert ok
    assert resultado == 5

def test_validar_id_no_entero():
    ok, mensaje = validar_id("abc")
    assert not ok
    assert mensaje == "El ID debe ser un número entero positivo."

def test_validar_id_negativo():
    ok, mensaje = validar_id("-2")
    assert not ok
    assert mensaje == "El ID debe ser un número entero positivo."