# SGPN - Sistema de Gestión de Pacientes y Nutrición

Sistema integral de gestión clínica y nutricional desarrollado para profesionales de la salud y nutricionistas, enfocado en el seguimiento antropométrico, historial clínico detallado, control de citas, pagos y analíticas en tiempo real.

## 🚀 Stack Tecnológico

- **Backend**: Python 3.10+, Flask 3.x, Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Gunicorn
- **Base de Datos**: SQLite (desarrollo/producción ligera) con ORM SQLAlchemy
- **Frontend**: HTML5, Tailwind CSS (diseño moderno y responsivo), Alpine.js (interactividad dinámica), Jinja2 templates
- **Arquitectura**: Clean Architecture / Patrón Controller-Model-View (Modular)

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
```python
python update_db_schema.py
```
O mediante Flask-Migrate:
```bash
flask db upgrade
```

### 5. Ejecutar el Servidor Local
```bash
python run.py
```
El sistema estará disponible en `http://127.0.0.1:5000`.

---

## 📁 Módulos Principales del Sistema

1. **Dashboard Principal (`/`)**: KPIs en tiempo real (crecimiento mensual, valoraciones del mes, promedio diario), pacientes en seguimiento, pacientes sin valoración reciente, citas del día con acciones rápidas y gráfico de actividad reciente.
2. **Gestión de Pacientes (`/pacientes`)**: Registro de nuevos pacientes, expedientes completos, listados de activos e inactivos, historial médico y agendamiento de citas.
3. **Valoración Antropométria (`/valoraciones`)**: Registro y seguimiento por pestañas (antropometría, pliegues cutáneos, signos vitales), mapa corporal interactivo y comparativas automáticas vs. consulta anterior (`to_dict()` para serialización JSON segura).
4. **Historial Clínico (`/historial-clinico`)**: Registro detallado de antecedentes quirúrgicos, padecimientos, medicamentos, suplementos, hábitos de actividad física y pautas nutricionales.
5. **Control de Pagos y Finanzas (`/pagos`)**: Registro de cobros, adeudos y estatus de cuentas por paciente.
6. **Agenda y Citas (`/citas`)**: Calendario y gestión de citas diarias.
