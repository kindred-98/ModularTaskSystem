![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white) 
![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white) 
![VSCode](https://img.shields.io/badge/Editor-VSCode-007ACC?logo=visual-studio-code&logoColor=white) 
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) 
![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white) 
![Windows](https://img.shields.io/badge/OS-Windows-0078D6?logo=windows&logoColor=white) 
![OneDrive](https://img.shields.io/badge/OneDrive-Sync-0078D4?logo=microsoft-onedrive&logoColor=white) 
![Modular](https://img.shields.io/badge/Arquitectura-Modular-green) 
![Clean Code](https://img.shields.io/badge/Clean%20Code-Prácticas%20Aplicadas-brightgreen) 
![CLI App](https://img.shields.io/badge/CLI-App-lightgrey) 
![README](https://img.shields.io/badge/Documentación-README-important)


# 📝 TODO List Modular en Python

Este proyecto es una **aplicación de lista de tareas (TODO)** organizada siguiendo principios de **modularización y Clean Code**.  
El objetivo es separar responsabilidades en diferentes módulos y carpetas, haciendo que el código sea **mantenible y escalable**.

---

## 📂 Estructura del proyecto

```
Modularizacion_De_tarea2/
│
├── run.py
├── pytest.ini
├── requirements.txt
│
└── src/
    ├── __init__.py
    ├── main.py
    │
    ├── ui/
    │   ├── __init__.py
    │   └── menu.py
    │
    ├── services/
    │   ├── __init__.py
    │   └── tareas_service.py
    │
    ├── data/
    │   ├── __init__.py
    │   └── storage.py
    │
    ├── utils/
    │   ├── __init__.py
    │   └── validators.py
    │
    └── tests/
        ├── test_services.py
        ├── test_storage.py
        └── test_validators.py

```

## 🚀Cómo ejecutar la aplicación

✔ Opción recomendada

``` 
python run.py
``` 
✔ Opción alternativa
``` bash
python -m src.main
```

## 🧪 Cómo ejecutar los tests

``` 
pytest
``` 
``` 
python -m pytest
``` 

## ⚙️ Funcionalidades

1) Añadir tareas
2) ompletar tareas
3) Eliminar tareas
4) Listar todas las tareas
5) Validación de entradas (descripción mínima, ID válido)
6) Almacenamiento en memoria mediante una lista interna
7) Servicios separados para lógica de negocio
8) Menú interactivo en consola

🛠️ Dependencias

Python >= 3.10
Opcional: pytest para tests
pytest>=7.0.0

## 📖 Prompts y requerimientos usados

1) Inicialmente: Modularización de código Python para separar responsabilidades.
2) Estructura de carpetas src/, data/, services/, utils/, ui/, tests/.
3) Implementación de validadores, storage, servicios y menú con docstrings.
4) Resolución de errores de imports en Windows con imports absolutos o sys.path.
5) Generación de README y documentación de todo el proyecto.
6) Corrección de errores de imports en Windows mediante imports absolutos.
7) Creación de un archivo run.py como punto de entrada estable.
8) Configuración de pytest.ini para asegurar que pytest detecte el paquete src.
9) Estructura profesional y mantenible siguiendo buenas prácticas.


## ✅ Buenas prácticas

- Código modular y separado por responsabilidades
- Uso de docstrings en todas las funciones
- Almacenamiento temporal en memoria (storage.py)
- Separación clara entre lógica de negocio y presentación.
- Preparado para agregar tests en carpeta tests/
- Compatible con Windows y ejecución directa desde main.py
- Tests unitarios para validadores, almacenamiento y servicios.
- Estructura compatible con Windows, Linux y macOS.
- Ejecución estable mediante run.py o python -m src.main.

# 📜 Licencia MIT
Proyecto educativo. Uso libre para aprendizaje, clase de DiCampus con RUSGAR sobre la IA aplicada a la progamacion.