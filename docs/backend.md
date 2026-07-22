# Documentación del Backend (Flask)

El backend del sistema está construido sobre **Flask**, estructurado bajo un patrón de controladores y modelos para separar la lógica de negocio de la persistencia de datos.

## Estructura de Controladores (`app/controllers/`)
Los controladores gestionan las rutas, procesan las solicitudes HTTP y coordinan la interacción con los modelos.

*   **`pacientes.py`**: Gestiona el ciclo de vida del paciente, incluyendo:
    *   Registro y edición de datos personales.
    *   Gestión de pagos.
    *   Carga masiva de valoraciones antropométricas vía Excel.
    *   **Gestión de Citas:** Implementa validaciones de disponibilidad y prevención de duplicados.

## Validaciones y Manejo de Errores
El sistema implementa validaciones defensivas en el servidor:

1.  **Validación de Datos:** Se verifica la integridad de los datos (ej. formato de teléfono, rangos de hora para citas) antes de interactuar con la base de datos.
2.  **Manejo de Errores:** Se utilizan bloques `try/except` para capturar excepciones durante las operaciones de base de datos.
3.  **Feedback al Usuario:** Se emplea `flash()` para enviar mensajes de estado (`success`, `error`, `warning`) que se renderizan en la interfaz.

## Flujo de Citas (Ejemplo)
```python
@pacientes.route('/<int:id>/registrar_proxima_cita', methods=['POST'])
def registrar_proxima_cita(id):
    # 1. Validación de campos obligatorios
    # 2. Validación de lógica de negocio (fecha, rango horario)
    # 3. Verificación de existencia previa (Cita.obtener_siguiente_cita)
    # 4. Verificación de disponibilidad (Cita.es_horario_disponible)
    # 5. Persistencia o retorno de mensaje de advertencia
```
