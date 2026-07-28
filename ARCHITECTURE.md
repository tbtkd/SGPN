# ARCHITECTURE.md - Arquitectura del Sistema SGPN

## 1. Arquitectura de Software y Patrones de Diseño

El sistema **SGPN (Sistema de Gestión de Pacientes y Nutrición)** está construido bajo el patrón **Clean Architecture / Controller-Model-View (Modular)**, desacoplando estrictamente las responsabilidades para garantizar mantenibilidad, escalabilidad y testabilidad.

```
SistemaPacientes/
├── app/
│   ├── __init__.py          # Fábrica de aplicaciones Flask (create_app) y registro de extensiones
│   ├── config.py            # Configuración de entornos (Development, Testing, Production)
│   ├── db.py                # Inicialización de SQLAlchemy (db_orm)
│   ├── logger.py            # Configuración centralizada de logs
│   ├── schema.sql           # Esquema relacional base en SQLite
│   ├── controllers/         # Lógica de negocio y controladores por módulo
│   ├── models/              # Modelos de ORM SQLAlchemy (Paciente, Valoracion, PlantillaMensaje, etc.)
│   ├── routes/              # Definición de Blueprints y endpoints HTTP
│   ├── static/              # Archivos estáticos organizados (CSS, JS desacoplado, imágenes)
│   └── templates/           # Vistas Jinja2 organizadas en layouts, componentes (_partials) y vistas modulares
├── tests/                   # Suite de pruebas unitarias (unittest)
├── docs/                    # Documentación técnica y diagramas de arquitectura
└── run.py                   # Punto de entrada de la aplicación
```

---

## 2. Esquema de Base de Datos y ORM

El sistema utiliza **SQLite** como motor relacional gestionado a través de **Flask-SQLAlchemy**. Los modelos principales implementados son:

- **`Paciente`**: Almacena información demográfica, de contacto, estatus (`activo`, `seguimiento`, `inactivo`) y relaciones con valoraciones e historiales.
- **`ValoracionAntropometrica`**: Almacena métricas por pestañas (antropometría, pliegues cutáneos, signos vitales) con serialización segura (`to_dict()`).
- **`PlantillaMensaje`**: Gestiona las plantillas de WhatsApp con campos `titulo`, `contenido` y `esta_activa` (asegurando exclusividad de plantilla activa).
- **`BitacoraContacto`**: Registro histórico de comunicaciones con pacientes.
- **`Cita` / `Pago` / `HistorialClinico`**: Módulos transaccionales y clínicos complementarios.

---

## 3. Estándares de Frontend y UI/UX

- **Diseño Responsivo**: Implementado con **Tailwind CSS** utilizando contenedores optimizados (`max-w-7xl`, `max-w-8xl`).
- **Interactividad Dinámica**: Uso de **Alpine.js** para modales reactivos, pestañas de navegación y validaciones en tiempo real en formularios complejos (como la Nueva Valoración Antropométrica).
- **Desacoplamiento de Scripts**: Todo el código JavaScript se encuentra estructurado en archivos `.js` dedicados dentro de `app/static/js/` (ej. `detalle_paciente.js`, `plantillas.js`, `dashboard.js`, `valoracionValidacion.js`), evitando scripts embebidos en plantillas Jinja2 y manteniendo alta legibilidad.
- **Manejo de Errores y Validaciones**: Validación defensiva en controladores backend con manejo de excepciones `try/except` y mensajes flash, complementada con auditoría en frontend, auto-focus en inputs erróneos y cambio automático de pestañas.
