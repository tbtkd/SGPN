# Arquitectura del Sistema (SGPN)

Este documento detalla los patrones arquitectónicos, las decisiones de diseño y los estándares tecnológicos aplicados en el **Sistema de Gestión de Pacientes Nutriológicos (SGPN)**.

---

## 1. Patrón Arquitectónico Backend: Controlador Modular en Flask

El backend se rige bajo un enfoque **Model-View-Controller (MVC)** adaptado para un desarrollo ágil y acoplado de forma nativa con SQLite y el motor de plantillas Jinja2 de Flask.

### Componentes de la Arquitectura
*   **Enrutamiento y Controladores (`app/controllers/`):** El sistema divide lógicamente las rutas y la lógica de negocio por dominios principales:
    *   `auth.py`: Manejo de autenticación, cierres de sesión y validación de credenciales.
    *   `pacientes.py`: Procesamiento de expedientes, estados activos/inactivos e historial clínico.
    *   `valoracion_antropometrica.py`: Registro de mediciones físicas, procesamiento de IMC, composición y tendencias de progreso.
    *   `main.py`: Consolidación del Dashboard clínico diario, alertas operativas y listados consolidados.
*   **Modelos y Base de Datos (`app/models/` y `app/db.py`):** SQLite como motor transaccional de lectura/escritura veloz y confiable. Las consultas están estrictamente parametrizadas para evitar ataques de inyección SQL.

---

## 2. Arquitectura de Plantillas (Jinja2 Modular por Dominios)

Para evitar la creación de archivos gigantescos monolíticos ("spaghetti HTML"), se ha implementado un esquema de herencia y modularización estricto basado en subcarpetas temáticas:

```text
app/templates/
├── base/
│   └── base.html                   # Contenedor global de layouts y scripts
├── dashboard/
│   ├── tabs/
│   │   ├── _pacientes_dia.html     # Tab: Citas de hoy
│   │   ├── _pendientes_agendar.html# Tab: Pacientes sin cita futura
│   │   └── _sin_valoracion.html    # Tab: Pacientes de nuevo ingreso
│   └── dashboard.html              # Layout de 2 columnas de la página principal
├── pacientes/
│   ├── nuevo_paciente.html         # Formulario de alta
│   ├── detalle_paciente.html       # Visualización de expediente central
│   └── partials/
│       ├── _historia_clinica.html  # Bloque modular de antecedentes
│       └── _lista_citas.html       # Bloque modular de agenda
└── valoraciones/
    ├── nueva_valoracion.html       # Formulario por pestañas
    ├── detalle_valoracion.html     # Layout de visualización de consulta
    └── partials/
        ├── _info_general.html      # Cabecera resumida de la valoración
        ├── _mapa_antropometrico.html# Mapa visual anatómico en 3 columnas
        └── _historial_valoraciones.html # Listado de valoraciones previas
```

### Reglas de Diseño de Plantillas
- **Modularidad:** Todo componente complejo o sección de información repetitiva debe residir en un archivo parcial (`_nombre_parcial.html`) e incluirse utilizando `{% include %}` o `{% with %}`.
- **Seguridad en Jinja2:** Se prohíbe el acceso directo a claves que puedan no existir. Es mandatorio utilizar el método `.get()` con valores por defecto y conversiones seguras:
  `valoracion.get('cintura', 0)|float(0)`

---

## 3. Patrón de Maquetación y Reactividad UI/UX

El frontend está diseñado para ofrecer una experiencia fluida, rápida y estéticamente impecable mediante un stack moderno y sin sobrecarga ("No-SPA"):

### Tecnologías en Frontend
- **Tailwind CSS (Estilos):** Permite construir una interfaz sofisticada sin necesidad de escribir hojas de estilo redundantes. Toda la paleta del sistema gira en torno al **Teal (Verde Azulado)** como color principal de acento, combinado con grises suaves para las tarjetas de información.
- **Alpine.js (Reactividad Ligera):** Utilizado para el manejo de estados locales que ocurren dentro de la página, eliminando la necesidad de frameworks robustos (React/Vue). Ejemplos:
  - Apertura/Cierre y colapsado dinámico del Sidebar.
  - Alternancia entre las pestañas (Tabs) operacionales del Dashboard y del formulario de Nueva Valoración.
  - Almacenamiento local de la visibilidad de menús.
- **JavaScript (Vanilla JS):** Lógica encargada de interceptar eventos globales como el envío de formularios para realizar auditorías visuales antes de que el servidor reciba la petición.

---

## 4. Estándares Visuales y de Diseño Corporativo

Para mantener la consistencia estética en todas las secciones desarrolladas, se han estandarizado las siguientes reglas:

### Contenedor Global
Todas las páginas internas heredan de `base.html` y deben agrupar su contenido principal bajo la clase unificada de ancho extendido:
```html
<div class="max-w-8xl mx-auto">
```

### Sidebar Fijo e Inteligente
- **Estructura:** Posee la propiedad `sticky top-0 h-screen`, permaneciendo estático en el lateral izquierdo mientras el contenido principal fluye verticalmente.
- **Colapso Dinámico:** Implementado con Alpine.js (`sidebarOpen`), de forma que el profesional de la nutrición pueda expandir su espacio de trabajo en pantallas reducidas.
- **Botón de Salida:** Ubicado en el pie del Sidebar (footer) de forma elegante, consistente y aislada para evitar cierres de sesión accidentales.

### Formato Unificado de Fechas
- **Estándar:** Toda fecha mostrada en el sistema debe seguir el formato de máscara legible: `DD MMM, YYYY` (ejemplo: `24 Jul, 2026`).
- **Hora Independiente:** La hora no debe unirse con guiones a la fecha. Si se requiere mostrar la hora de una cita, se debe renderizar en un badge o elemento visual separado para optimizar la legibilidad.
