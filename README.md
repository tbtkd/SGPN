# Sistema de Gestión de Pacientes y Nutrición (SGPN)

Sistema web profesional desarrollado para la administración integral de pacientes, control de valoraciones antropométricas avanzadas, agenda de citas médicas, registro de pagos y seguimiento clínico por WhatsApp.

## Stack Tecnológico

- **Backend:** Python 3.10+, Flask, Flask-SQLAlchemy, Flask-Migrate
- **Base de Datos:** SQLite (`instance/sgpn_nutricion.db`), ORM SQLAlchemy
- **Frontend:** Tailwind CSS, Alpine.js, Jinja2 Templates, FontAwesome
- **Herramientas de Procesamiento:** OpenPyXL (importación masiva de valoraciones desde Excel)

## Guía Rápida de Instalación y Ejecución

1. **Clonar el repositorio y acceder al directorio:**
   ```bash
   cd SistemaPacientes
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/macOS:
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno (opcional/desarrollo):**
   Crear un archivo `.env` o usar el archivo `config.py` por defecto.

5. **Ejecutar el servidor de desarrollo:**
   ```bash
   python run.py
   ```
   El sistema estará disponible en `http://127.0.0.1:5000`.

## Módulos Principales

- **Gestión de Pacientes:** Registro, edición, activación/inactivación, búsqueda en tiempo real, perfil detallado.
- **Valoraciones Antropométricas:** Formulario por pestañas con validación defensiva en backend y frontend (interceptación de submit, cambio automático de pestaña ante errores, `.focus()` y estilos de error), importación masiva vía Excel.
- **Agenda y Citas:** Programación, validación de horarios disponibles, control de estados (pendiente, completada, cancelada).
- **Control Financiero:** Registro de pagos asociados a pacientes.
- **Bitácora de WhatsApp:** Seguimiento e historial de acompañamiento clínico.
