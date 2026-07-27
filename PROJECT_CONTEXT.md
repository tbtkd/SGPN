<!--
AI INSTRUCTION: Antes de realizar cualquier modificación al código, lee este archivo para alinearte con las decisiones arquitectónicas y de diseño ya tomadas. No rompas los estándares establecidos aquí bajo ninguna circunstancia.
-->

# MEMORIA DE CONTINUIDAD Y CONTEXTO DEL PROYECTO (SGPN)

Este documento sirve como la **Memoria Viva** y fuente de verdad técnica del **Sistema de Gestión de Pacientes Nutriológicos (SGPN)** para la clínica de la especialista **Aurora Ángeles**. Todo desarrollador o modelo de IA debe respetar y continuar las decisiones y estándares documentados a continuación.

---

## 1. Estado Actual del Proyecto (Logros y Avances)

Se ha completado la refactorización profunda de las interfaces clave del sistema, logrando una consistencia visual de nivel premium y mejorando la robustez del servidor:

- **Refactorización del Sidebar:** Implementación de un Sidebar fijo (`sticky top-0 h-screen`), colapsable de forma fluida mediante Alpine.js, almacenamiento de estado local y reubicación del botón "Salir" en el pie del menú con un diseño profesional y seguro.
- **Rediseño del Dashboard Clínico:** Organización de la página principal en un Layout de 2 columnas (8/4) balanceado. Implementación del sistema de pestañas reactivas (Alpine.js) para clasificar dinámicamente a los pacientes: *Pacientes del Día*, *Pendientes por Agendar* y *Sin Valoración*.
- **Reestructuración del Mapa Antropométrico:** Transformación del componente visual de visualización de mediciones en un layout de 3 columnas anatómicas:
  1. *Columna Izquierda:* Perímetros corporales (Cintura, Tórax, Brazo, Cadera, Pierna, Pantorrilla).
  2. *Columna Central:* Silueta interactiva de calor (Body Map).
  3. *Columna Derecha:* Pliegues cutáneos (Bíceps, Tríceps, Suprailíaco, Subescapular, Femoral).
- **Protección y Tolerancia a Fallos en Plantillas (Evitar Error 500):** Modificación de las plantillas Jinja2 para utilizar accesos seguros `.get()` y conversiones seguras con valores por defecto como `|float(0)` para que la UI no se rompa si se cargan valoraciones incompletas o nulas.
- **Unificación Estética de Fechas:** Aplicación sistemática del formato de máscara `"DD MMM, YYYY"` (ejemplo: `"24 Jul, 2026"`) y aislamiento de la hora en badges específicos independientes.

---

## 2. Decisiones de Diseño y UI/UX (Reglas Inquebrantables)

Cualquier cambio o nueva funcionalidad debe alinearse estrictamente con las siguientes directrices:

### 📐 Estructura de Contenedores y Layouts
- **Ancho Máximo de Páginas:** Todo contenedor principal debe envolverse con la clase Tailwind:
  `class="max-w-8xl mx-auto"` (prohibido usar `max-w-7xl` o anchos móviles por defecto en páginas completas).
- **Consistencia del Sidebar:** El Sidebar debe permanecer inalterado en su posición izquierda, fijado a la pantalla (`sticky top-0 h-screen`).

### 🎨 Paleta de Colores y Estilo Visual
- **Color de Acento:** El color institucional de la clínica es el **Teal (Verde azulado)**. Se deben emplear clases como `bg-teal-600`, `text-teal-700`, `hover:bg-teal-700`, `border-teal-100`, etc.
- **Tarjetas e Información:** Uso de fondos blancos (`bg-white`), bordes ultra-suaves (`border-gray-100`) y sombras minimalistas (`shadow-sm`) con esquinas redondeadas pronunciadas (`rounded-2xl`).

### 📂 Estructura de Archivos y Parciales (Prohibición de Monolitos)
- Está estrictamente **prohibido** escribir bloques de código de más de 300 líneas de HTML en un solo archivo de plantilla.
- Si una sección tiene complejidad lógica o agrupa información temática específica, debe ser extraída a la subcarpeta `partials/` o `tabs/` del módulo correspondiente e importarse con `{% include %}`.

### 📅 Formato de Fechas y Horas
- Las fechas siempre deben mostrarse en formato amigable español, ej: `24 Jul, 2026` (nunca formatos ISO raw como `2026-07-24` directamente al usuario).
- Las horas de citas o registros deben presentarse de forma independiente a la fecha, idealmente encapsuladas en un badge gris o teal suave (`bg-gray-100 text-gray-700 px-2 py-1 rounded`).

---

## 3. Backlog de Próximos Pasos (Pendientes)

Para las siguientes etapas de desarrollo, se tienen planificadas las siguientes mejoras y módulos:

1. **Gráficos Históricos Dinámicos:** Integrar Chart.js en la vista de expediente del paciente para trazar la curva de progreso de Peso, % de Grasa e IMC de forma interactiva.
2. **Exportador de Reportes PDF:** Generación de un reporte PDF estético y descargable con el resumen del Mapa Antropométrico y diagnóstico del paciente para poder ser enviado por correo o impreso.
3. **Módulo de Planificación Dietética:** Creación de un planificador de menús semanales basado en equivalentes calóricos directamente asociado al expediente del paciente.
4. **Optimización de Citas:** Calendario interactivo mensual (estilo FullCalendar) para una visualización más cómoda de la agenda de consultas de la clínica.
