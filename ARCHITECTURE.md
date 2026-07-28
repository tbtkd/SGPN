# Arquitectura del Sistema - SGPN

Este documento detalla la arquitectura de software, organización de carpetas, esquema de base de datos y estándares de diseño del **Sistema de Gestión de Pacientes y Nutrición (SGPN)**.

---

## 1. Arquitectura de Software

El proyecto sigue una adaptación modular de **Clean Architecture** estructurada en Flask bajo el patrón **Controller-Model-View (CMV)**:

- **Modelos (`app/models/`)**: Entidades de SQLAlchemy que representan las tablas relacionales y encapsulan lógica de negocio orientada a datos (ej. métodos estáticos de consulta, validación y serialización como `to_dict()`).
- **Controladores / Blueprints (`app/controllers/` y `app/routes/`)**: Capa de aplicación que gestiona las peticiones HTTP, validación defensiva de `request.form`, control de excepciones con `try/except`, mensajería flash (`flash()`) y renderizado de vistas.
- **Vistas (`app/templates/`)**: Plantillas Jinja2 organizadas jerárquicamente en componentes reutilizables (`components/`), pestañas (`tabs/`) y particiones (`partials/`).

---

## 2. Estructura de Directorios

```text
SistemaPacientes/
│
├── app/
│   ├── __init__.py           # Fábrica de aplicación (create_app), extensiones (db, login_manager)
│   ├── config.py             # Configuración de entornos
│   ├── db.py                 # Inicialización de SQLAlchemy
│   ├── schema.sql            # Script SQL base de respaldo
│   ├── controllers/          # Blueprints y lógica de rutas (main, pacientes, valoraciones, etc.)
│   ├── models/               # Modelos ORM (Paciente, ValoracionAntropometrica, Cita, Pago, HistorialClinico)
│   ├── static/               # Activos estáticos (CSS con Tailwind, JS modular, imágenes, logos)
│   ├── templates/            # Plantillas Jinja2
│   │   ├── base/             # Layouts base (base.html con sidebar y navegación)
│   │   ├── dashboard/        # Pantalla principal y subcarpetas `tabs/`
│   │   ├── pacientes/        # Gestión de pacientes y expedientes
│   │   ├── valoraciones/     # Formularios de valoración y subcarpeta `partials/`
│   │   └── components/       # Componentes visuales reutilizables (ej. body_map.html)
│   └── utils/                # Utilidades, filtros de Jinja (formateo de fechas, etc.)
├── migrations/               # Control de migraciones con Flask-Migrate / Alembic
├── run.py                    # Punto de entrada de la aplicación
├── requirements.txt          # Dependencias de Python
└── PROJECT_CONTEXT.md        # Memoria viva del proyecto para desarrollo guiado por LLM
```

---

## 3. Esquema de Base de Datos y ORM

El sistema utiliza **SQLite** con relaciones ORM estrictas:

- **`pacientes`**: Tabla principal con datos demográficos, antropometría inicial, estatus (activo/inactivo/seguimiento).
- **`valoracion_antropometrica`**: Relacionada con `pacientes` (CASCADE), almacena medidas detalladas por cita, pliegues cutáneos, IMC y el método `to_dict()` para interoperabilidad con Alpine.js.
- **`historial_clinico`**: Relación 1:1 con `pacientes`, almacena antecedentes patológicos, quirúrgicos, medicamentos, suplementos y hábitos de actividad física.
- **`citas`**: Agenda vinculada a `pacientes` con fecha, hora y estado (`pendiente`, `completada`, etc.).
- **`pagos`**: Control financiero de cobros y saldos por paciente.

---

## 4. Estándares de Frontend y UI/UX

- **Contenedor Principal**: Uso estandarizado de clases con ancho extendido (`max-w-8xl` o fluidas) para aprovechar pantallas de escritorio de alta resolución.
- **Navegación**: Sidebar colapsable y barra superior con indicador de usuario activo y notificaciones.
- **Formularios por Pestañas**: Validación en Frontend mediante JavaScript que audita campos requeridos, conmuta automáticamente a la pestaña oculta con errores, aplica foco (`.focus()`) y estilos visuales de error.
- **Interactividad**: Alpine.js para componentes reactivos en cliente (mapa antropométrico corporal, modales, pestañas) y Tailwind CSS para diseño utilitario moderno.
- **Tipado y Serialización**: Conversión explícita de objetos ORM a diccionarios mediante `to_dict()` antes de inyectarlos como JSON en directivas `x-data`.
