# Documentación del Frontend (SGPN)

## 1. Arquitectura y Componentes UI/UX
El frontend se estructura utilizando **Jinja2** para plantillas modulares, **Tailwind CSS** para diseño responsivo y **Alpine.js** para la gestión de interactividad y estado local en componentes dinámicos.

### Estructura de Estilos y Vistas (`app/static/`)
- **Componentes modulares (`app/static/css/components/`):**
  - `_buttons.css`, `_cards.css`, `_forms.css`, `_modal.css`, `_tables.css`, `_tabs.css`, `base.css`.
- **Sidebar y Navegación:**
  - Barra lateral con diseño colapsable, indicadores de sesión y acceso directo al nuevo ítem de navegación **"Plantillas de Mensajes"** para gestionar el catálogo de WhatsApp.

---

## 2. Características Interactivas Clave

### 2.1. Modal de Envío de WhatsApp con Inyección de Variables
- Permite al usuario enviar mensajes predeterminados directamente a WhatsApp Web.
- **Inyección Automática:** Sustituye etiquetas como `{nombre}` por el nombre del paciente y `{dias}` por los días transcurridos desde su última cita.
- Registra automáticamente la interacción en la bitácora del sistema tras el envío.

### 2.2. Modal de Agendamiento y Validación de Horarios en Tiempo Real
- Al seleccionar una fecha en el calendario de citas, el sistema realiza una petición asíncrona (`/pacientes/disponibilidad_horas`) para consultar las horas ocupadas.
- Desactiva y marca visualmente las opciones correspondientes en el `<select>` de horarios, previniendo la duplicidad de citas en el mismo bloque horario.
- Cuenta con validación previa de citas pendientes existentes para emitir alertas o modales de confirmación al intentar reagendar.

### 2.3. Formulario de Valoración Antropométrica por Pestañas
- **Intercepción de Submit:** El script de validación audita todos los campos requeridos distribuidos en las 3 pestañas (Antropométrica, Plicometría, Bioimpedancia).
- **Navegación Automática:** Si detecta un campo vacío o inválido, cambia automáticamente a la pestaña oculta contenedora, aplica `.focus()` y `scrollIntoView()` en el input afectado, y despliega indicadores visuales de error.
