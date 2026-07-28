# SGPN - Sistema de Gestión de Pacientes y Nutrición

Sistema integral de gestión clínica y nutricional desarrollado para profesionales de la salud y nutricionistas, enfocado en el seguimiento antropométrico, historial clínico detallado, control de citas, pagos, bitácoras de WhatsApp con plantillas dinámicas y analíticas en tiempo real.

## 🚀 Stack Tecnológico

- **Backend**: Python 3.10+, Flask 3.x, Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Gunicorn
- **Base de Datos**: SQLite (desarrollo/producción ligera) con ORM SQLAlchemy
- **Frontend**: HTML5, Tailwind CSS (diseño moderno y responsivo con contenedor máximo optimizado), Alpine.js (interactividad dinámica y modales), Jinja2 templates (con JavaScript desacoplado en archivos estáticos)
- **Arquitectura**: Clean Architecture / Patrón Controller-Model-View (Modular) con pruebas unitarias (`unittest`)

---

## 🛠️ Guía Rápida de Instalación y Ejecución

### 1. Clonar el repositorio y configurar entorno virtual
```bash
git clone https://github.com/tbtkd/SGPN.git
cd SistemaPacientes
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/macOS:
source .venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto (o utiliza los valores por defecto en `config.py`):
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_super_segura
DATABASE_URL=sqlite:///pacientes.db
```

### 4. Inicializar y migrar la Base de Datos
```bash
python update_db_schema.py
```
O mediante Flask-Migrate:
```bash
flask db upgrade
```

### 5. Ejecutar Pruebas Unitarias
```python
python -m unittest discover tests
```

### 6. Ejecutar el Servidor Local
```bash
python run.py
```
El sistema estará disponible en `http://127.0.0.1:5000`.

---

## 📁 Módulos Principales del Sistema

1. **Dashboard Principal (`/`)**: KPIs en tiempo real (crecimiento mensual, valoraciones del mes, promedio diario), pacientes en seguimiento, pacientes sin valoración reciente, citas del día con acciones rápidas y gráfico de actividad reciente.
2. **Gestión de Pacientes (`/pacientes`)**: Registro de nuevos pacientes, expedientes completos, listados de activos e inactivos, historial médico, agendamiento de citas con disponibilidad horaria dinámica y bitácoras de acompañamiento por WhatsApp.
3. **Valoración Antropométrica (`/valoraciones`)**: Registro y seguimiento con validación defensiva en backend y frontend por pestañas (antropometría, pliegues cutáneos, signos vitales), mapa corporal interactivo y cálculo automático de IMC.
4. **Historial Clínico (`/historial-clinico`)**: Registro detallado de antecedentes quirúrgicos, padecimientos, medicamentos, suplementos, hábitos de actividad física y pautas nutricionales.
5. **Catálogo de Plantillas de WhatsApp (`/plantillas-mensajes`)**: Gestión de plantillas con variables dinámicas `{nombre}` y `{dias}`, y selección de plantilla activa por defecto.
6. **Control de Pagos y Finanzas (`/pagos`)**: Registro de cobros, adeudos y estatus de cuentas por paciente.
7. **Agenda y Citas (`/citas`)**: Calendario y gestión de citas diarias.
