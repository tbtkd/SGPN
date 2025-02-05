## pip freeze > requirements.txt 

## Sistema de Gestión de Pacientes Nutriológicos (SGPN)

## Descripción
Sistema web desarrollado en Flask para la gestión integral de pacientes en consultorios nutricionales. Permite el seguimiento detallado de valoraciones antropométricas, historiales clínicos y control administrativo.

## Características Principales
- Gestión completa de pacientes (CRUD)
- Registro y seguimiento de valoraciones antropométricas
- Cálculo automático de IMC
- Historial clínico detallado
- Importación masiva de datos desde Excel
- Interfaz responsiva y amigable
- Filtrado de pacientes por estado (activo/inactivo)

## Tecnologías Utilizadas
- Backend: Python 3.8+ con Flask
- Frontend: HTML5, CSS3, JavaScript
- Base de datos: SQLite
- Librerías principales: openpyxl, pandas
- Componentes UI: Alpine.js, Font Awesome

## Estructura del Proyecto
sistema_pacientes/
├── app/
│   ├── api/                    # Nueva carpeta para endpoints API
│   ├── core/                   # Lógica central de negocio
│   ├── utils/                  # Utilidades comunes
│   └── extensions.py           # Extensiones Flask (SQLAlchemy, etc)
├── tests/                      # Pruebas unitarias
└── migrations/                 # Migraciones de base de datos
├── instance/                             # Base de datos SQLite
├── docs/                                 # Documentación
├── config.py                             # Configuraciones
└── run.py                                # Script de inicio

La aplicación se iniciará automáticamente en el navegador predeterminado.

### Funcionalidades Principales

#### Gestión de Pacientes
- Alta de nuevos pacientes con validación de datos
- Listado separado de pacientes activos e inactivos
- Búsqueda y filtrado de pacientes
- Edición y cambio de estado

#### Valoraciones Antropométricas
- Registro de medidas corporales
- Cálculo automático de IMC
- Historial de valoraciones
- Importación desde Excel

#### Historial Clínico
- Registro de antecedentes médicos
- Seguimiento de medicamentos
- Control de actividad física
- Hábitos alimenticios


## Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Navegador web moderno

### Pasos de Instalación
1. Clonar el repositorio

 * git clone [url-del-repositorio]
 * cd sistema_pacientes

2. Crear y activar entorno virtual:

  * python -m venv venv
  * source venv/bin/activate # Linux/Mac
  * venv\Scripts\activate # Windows

3. Instalar dependencias:

  * pip install -r requirements.txt

4. Configurar variables de entorno:

  * Linux/Mac
    - export FLASK_ENV=development # o production
    - export FLASK_APP=run.py

  * Windows
    - set FLASK_ENV=development
    - set FLASK_APP=run.py

### Ejecución
- Desarrollo:

  * Linux/Mac
    - ./run_dev.sh

  * Windows
    - run_dev.bat

## Cambios entre Desarrollo y Producción

### Para Desarrollo:
1. En `config.py`: Usar `DevelopmentConfig`
2. En `__init__.py`: Descomentar configuración de logging
3. Activar `DEBUG = True`
4. Usar base de datos de desarrollo

### Para Producción:
1. En `config.py`: Usar `ProductionConfig`
2. En `__init__.py`: Mantener comentada la configuración de logging
3. Asegurar `DEBUG = False`
4. Usar base de datos de producción
5. Configurar `SECRET_KEY` segura

## Mantenimiento
- Base de datos: SQLite (puede cambiarse a otro motor si se requiere)
- Logs: Desactivados por defecto, activar en desarrollo si se necesita
- Caché: Implementada para optimizar consultas frecuentes

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

## Licencia
[Especificar licencia]

##
Ofuscar el código
PyInstaller 
##

La aplicación se iniciará automáticamente en el navegador predeterminado.

### Funcionalidades Principales

#### Gestión de Pacientes
- Alta de nuevos pacientes con validación de datos
- Listado separado de pacientes activos e inactivos
- Búsqueda y filtrado de pacientes
- Edición y cambio de estado

#### Valoraciones Antropométricas
- Registro de medidas corporales
- Cálculo automático de IMC
- Historial de valoraciones
- Importación desde Excel

#### Historial Clínico
- Registro de antecedentes médicos
- Seguimiento de medicamentos
- Control de actividad física
- Hábitos alimenticios

## Mantenimiento

### Desarrollo