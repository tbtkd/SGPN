# Documentación del Frontend

La interfaz de usuario combina plantillas **Jinja2** con **JavaScript nativo** y **Alpine.js** para ofrecer una experiencia dinámica y responsiva.

## Interacción y Componentes
*   **Plantillas (Jinja2):** Renderizan los datos del backend y estructuran el DOM.
*   **JavaScript (Vanilla):** Utilizado para la lógica de interacción compleja, como la gestión de modales, validaciones de formularios en tiempo real y peticiones asíncronas (`fetch`).
*   **Alpine.js:** Utilizado para componentes reactivos ligeros en la interfaz.

## Validaciones y Navegación
El sistema implementa validaciones robustas para asegurar la integridad de los datos antes de enviarlos al servidor:

1.  **Validación de Formularios:**
    *   Se interceptan los eventos `submit` para validar campos requeridos.
    *   Se aplican estilos visuales (clases CSS) para indicar errores.
    *   Se utiliza `.focus()` para dirigir al usuario al campo con error.

2.  **Gestión de Citas (Flujo de Validación):**
    *   Al hacer clic en "Registrar Próxima Cita", el frontend verifica si el paciente ya tiene una cita activa.
    *   Si existe, se muestra una alerta (`alert`) impidiendo la duplicación y sugiriendo la actualización.
    *   Se utiliza `fetch` para consultar la disponibilidad de horarios en tiempo real al seleccionar una fecha.

## Diagrama de Flujo de Citas (Frontend)

```mermaid
graph TD
    A[Clic en Registrar Cita] --> B{¿Tiene cita previa?}
    B -- Sí --> C[Mostrar Alerta: Usar Actualizar]
    B -- No --> D[Abrir Modal de Registro]
    D --> E[Seleccionar Fecha]
    E --> F[Consultar Disponibilidad (Fetch)]
    F --> G{¿Horario Disponible?}
    G -- No --> H[Deshabilitar Hora]
    G -- Sí --> I[Habilitar Hora]
```
