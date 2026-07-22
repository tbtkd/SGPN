# Sistema de Gestión de Pacientes Nutriológicos (SGPN)

## Descripción
Sistema web desarrollado en Flask para la gestión integral de pacientes en consultorios nutricionales. Permite el seguimiento detallado de valoraciones antropométricas, historiales clínicos, control de pagos y programación de citas.

## Características Principales
- Gestión completa de pacientes (CRUD)
- Registro y seguimiento de valoraciones antropométricas
- Cálculo automático de IMC
- Historial clínico detallado
- Importación masiva de datos desde Excel
- Programación y actualización de citas con validación de disponibilidad
- Interfaz responsiva y amigable
- Filtrado de pacientes por estado (activo/inactivo)

## Tecnologías Utilizadas
- **Backend:** Python 3.8+ con Flask
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Alpine.js
- **Base de datos:** SQLite
- **Librerías principales:** `openpyxl`

## Estructura del Proyecto
```text
SistemaPacientes/
├── app/
│   ├── controllers/  # Lógica de negocio y rutas
│   ├── models/       # Modelos de datos (ORM/SQL)
│   ├── static/       # Archivos estáticos (JS, CSS)
│   └── templates/    # Plantillas HTML (Jinja2)
├── docs/             # Documentación técnica
├── config.py         # Configuraciones
└── run.py            # Script de inicio
```

## Documentación Modular
*   [Backend (Controladores y Lógica)](docs/backend.md)
*   [Frontend (Interfaz y Validaciones)](docs/frontend.md)

## Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación
1. Clonar el repositorio:
   `git clone [url-del-repositorio]`
   `cd SistemaPacientes`

2. Crear y activar entorno virtual:
   - `python -m venv .venv`
   - `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)

3. Instalar dependencias:
   `pip install -r requirements.txt`

### Ejecución
- `python run.py`

## Seguridad
- Sesiones seguras configuradas
- Validación de datos en frontend y backend
- Protección contra CSRF
- Sanitización de entradas de usuario

## Contribución
1. Fork del repositorio
2. Crear rama para nueva característica
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request
