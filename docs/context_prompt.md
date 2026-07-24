# Contexto del Proyecto: Sistema de Gestión de Pacientes (SGPN)

## Resumen del Estado Actual
El proyecto es un sistema de gestión de pacientes desarrollado en **Flask (Python)** con una interfaz dinámica utilizando **Tailwind CSS** y **Alpine.js**.

### Funcionalidades Recientes
1.  **Validación de Valoraciones:** Implementación de validaciones defensivas en el backend (`app/controllers/valoracion_antropometrica.py`) para asegurar la integridad de los datos antes de la persistencia.
2.  **Mapa Antropométrico Interactivo:**
    *   Conexión bidireccional entre la silueta SVG y las listas de datos (Perímetros y Pliegues) mediante **Alpine.js**.
    *   Resaltado visual dinámico al pasar el mouse sobre regiones del cuerpo o filas de datos.
    *   Comparativa automática con la valoración anterior, mostrando indicadores de cambio (aumento/disminución) con estilos visuales (colores Teal/Ámbar).

## Arquitectura y Convenciones
*   **Backend:** Patrón de controladores (`app/controllers/`) y modelos (`app/models/`). Uso de `flash()` para feedback al usuario y `try/except` para manejo de errores.
*   **Frontend:** Plantillas Jinja2, Tailwind CSS para estilos, y Alpine.js para interactividad ligera.
*   **Validaciones:** Conversión segura de tipos (`safe_float`, `safe_int`) y validación de campos obligatorios en el servidor.

## Documentación de Referencia
*   `docs/backend.md`: Detalles sobre la lógica de negocio y validaciones.
*   `docs/frontend.md`: Detalles sobre la interactividad y componentes de UI.

## Notas para Continuar el Desarrollo
*   Al realizar cambios en las plantillas, asegurar la conversión explícita de tipos (`|float`) antes de operaciones aritméticas para evitar `TypeError`.
*   Mantener la consistencia en el uso de Alpine.js para la interactividad del mapa antropométrico.
*   Cualquier nueva funcionalidad debe seguir el patrón de validación defensiva en el controlador.
