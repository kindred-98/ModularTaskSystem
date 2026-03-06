# 📝 TODO List Modular en Python

Este proyecto es una **aplicación de lista de tareas (TODO)** organizada siguiendo principios de **modularización y Clean Code**.  
El objetivo es separar responsabilidades en diferentes módulos y carpetas, haciendo que el código sea **mantenible y escalable**.

---

## 📂 Estructura del proyecto

```
src/
├── main.py                # Punto de entrada
├── data/
│   ├── __init__.py
│   └── storage.py         # Almacenamiento de tareas en memoria
├── services/
│   ├── __init__.py
│   └── tareas_service.py  # Lógica de manejo de tareas
├── utils/
│   ├── __init__.py
│   └── validators.py      # Funciones de validación
└── ui/
    ├── __init__.py
    └── menu.py            # Interfaz de usuario
tests/
├── __init__.py
├── test_validators.py
├── test_services.py
└── test_storage.py
requirements.txt
README.md

```

Cómo ejecutar la aplicación

1) Abrir la terminal en la raíz del proyect(Modularizacion_De_tarea2.py).

2) Ejecutar la app:

``` bash
cd src
python main.py
```

⚙️ Funcionalidades

1) Añadir tarea
2) Completar tarea
3) Eliminar tarea
4) Listar tareas
5) Validaciones de entrada (descripción y ID)
6) Almacenamiento en memoria (lista de Python)

🛠️ Dependencias

Python >= 3.10
Opcional: pytest para tests
pytest>=7.0.0

📖 Prompts y requerimientos usados

1) Inicialmente: Modularización de código Python para separar responsabilidades.
2) Estructura de carpetas src/, data/, services/, utils/, ui/, tests/.
3) Implementación de validadores, storage, servicios y menú con docstrings.
4) Resolución de errores de imports en Windows con imports absolutos o sys.path.
5) Generación de README y documentación de todo el proyecto.

✅ Buenas prácticas

- Código modular y separado por responsabilidades
- Uso de docstrings en todas las funciones
- Almacenamiento temporal en memoria (storage.py)
- Preparado para agregar tests en carpeta tests/
- Compatible con Windows y ejecución directa desde main.py