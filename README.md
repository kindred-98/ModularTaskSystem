<div align="center">

# 📋 TODO List Manager

Una aplicación de línea de comandos robusta y modular para la gestión de tareas pendientes, desarrollada en Python siguiendo las mejores prácticas de arquitectura de software y Clean Code.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-Pytest-0A9EDC?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Cross--Platform-lightgrey)

</div>

---
## 📖 Índice

- [🚀 Descripción](#-descripción)
- [✨ Características](#-características)
- [🏗️ Arquitectura](#️-arquitectura)
- [📦 Instalación](#-instalación)
- [🎯 Uso](#-uso)
- [🧪 Pruebas](#-pruebas)
- [🤝 Contribución](#-contribución)
- [📄 Licencia](#-licencia)
- [📞 Contacto](#-contacto)

---

## 🚀 Descripción

**TODO List Manager** es una aplicación CLI diseñada para ayudar a los usuarios a organizar y gestionar sus tareas diarias de manera eficiente. El proyecto demuestra principios de desarrollo de software profesional mediante una arquitectura modular que separa claramente las responsabilidades en capas distintas: interfaz de usuario, lógica de negocio, persistencia de datos y utilidades.

La aplicación permite crear, completar, eliminar y visualizar tareas, almacenándolas en memoria durante la sesión. Es ideal para aprender sobre patrones de diseño, modularización y testing en Python.

---

## ✨ Características

- ✅ **Gestión completa de tareas**: Crear, marcar como completadas, eliminar y listar tareas
- 🏗️ **Arquitectura modular**: Separación clara de responsabilidades (UI, Servicios, Datos, Utilidades)
- 🧪 **Suite de pruebas**: Cobertura completa con Pytest
- 🎨 **Interfaz intuitiva**: Menú CLI con diseño visual atractivo
- 🔒 **Validación robusta**: Entradas sanitizadas y manejo de errores
- 📊 **Persistencia en memoria**: Almacenamiento temporal eficiente
- 🚀 **Fácil de extender**: Estructura preparada para nuevas funcionalidades

---

## 🏗️ Arquitectura

El proyecto sigue una arquitectura en capas bien definida:

```
📁 src/
├── 🎯 main.py          # Punto de entrada de la aplicación
├── 🖥️ ui/
│   └── 📋 menu.py       # Interfaz de usuario y menú principal
├── ⚙️ services/
│   └── 🔧 tareas_service.py  # Lógica de negocio para tareas
├── 💾 data/
│   └── 🗄️ storage.py    # Capa de persistencia de datos
└── 🛠️ utils/
    └── ✅ validators.py # Utilidades de validación
```

### Principios aplicados:
- **Separación de responsabilidades**: Cada módulo tiene una función específica
- **Inyección de dependencias**: Servicios independientes y testeables
- **Clean Code**: Nombres descriptivos, funciones pequeñas, documentación clara
- **SOLID Principles**: Especialmente Single Responsibility y Dependency Inversion

---

## 📦 Instalación

### Prerrequisitos
- Python 3.10 o superior
- Git (opcional, para clonar el repositorio)

### Pasos de instalación

1. **Clona el repositorio** (o descarga los archivos):
   ```bash
   git clone https://github.com/tu-usuario/Modularizacion_De_tarea2.py.git
   cd Modularizacion_De_tarea2.py
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv .venv
   ```

3. **Activa el entorno virtual**:
   - **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```

4. **Instala las dependencias** (si hay alguna en el futuro):
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎯 Uso

### Ejecutar la aplicación

Una vez instalado, ejecuta la aplicación desde el directorio raíz:

```bash
python run.py
```

### Menú principal

Al iniciar, verás un menú interactivo:

```
╔══════════════════════════╗
║       TODO  LIST         ║
╠══════════════════════════╣
║ 1. Añadir tarea          ║
║ 2. Completar tarea       ║
║ 3. Eliminar tarea        ║
║ 4. Ver tareas            ║
║ 0. Salir                 ║
╚══════════════════════════╝
```

### Funcionalidades disponibles

1. **Añadir tarea**: Ingresa una descripción para crear una nueva tarea
2. **Completar tarea**: Marca una tarea como completada usando su ID
3. **Eliminar tarea**: Remueve una tarea de la lista usando su ID
4. **Ver tareas**: Muestra todas las tareas con su estado actual
5. **Salir**: Cierra la aplicación

### Ejemplo de uso

```
Opción: 1
Descripción: Comprar leche
✅ Tarea añadida exitosamente

Opción: 4
📋 Lista de tareas:
1. [ ] Comprar leche
```

---

## 🧪 Pruebas

El proyecto incluye una suite completa de pruebas unitarias usando Pytest.

### Ejecutar las pruebas

```bash
# Desde el directorio raíz con el entorno virtual activado
pytest
```

### Estructura de pruebas

```
📁 tests/
├── 🧪 test_services.py    # Pruebas para la lógica de servicios
├── 💾 test_storage.py     # Pruebas para la capa de datos
└── ✅ test_validators.py  # Pruebas para utilidades de validación
```

### Cobertura de pruebas

- ✅ Servicios de tareas (CRUD operations)
- ✅ Validación de entradas
- ✅ Persistencia de datos
- ✅ Manejo de errores

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### Guías de contribución

- Sigue los principios de Clean Code
- Añade pruebas para nuevas funcionalidades
- Actualiza la documentación según sea necesario
- Usa commits descriptivos

---

*Desarrollado usando Python y las mejores prácticas de desarrollo de software.*
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

---
<div align="center">

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Contacto

**Autor**: Ángel  
**Proyecto**: TODO List Manager  
**Repositorio**: [![GitHub](https://img.shields.io/badge/GitHub-kindred--98-181717?style=for-the-badge&logo=github)](https://github.com/kindred-98)

Para preguntas o sugerencias, abre un issue en el repositorio.

---
</div>
