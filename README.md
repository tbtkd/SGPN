# Panel de Control Clínico para Nutrición "Aurora Ángeles" (SGPN)

## Descripción
El **Sistema de Gestión de Pacientes Nutriológicos (SGPN)** es una plataforma web integral diseñada para la clínica de nutrición de la especialista **Aurora Ángeles**. El sistema optimiza los flujos de trabajo diarios del consultorio, permitiendo la gestión eficiente del ciclo de vida del paciente: desde su registro e historia clínica, la programación inteligente de citas, hasta la medición y visualización detallada del progreso antropométrico mediante indicadores avanzados e interactivos.

---

## Características Principales

### 🖥️ Dashboard Clínico Reactivo
- **Layout de 2 Columnas (8/4):** Panel principal optimizado para monitoreo y agenda en tiempo real.
- **Pestañas Operacionales:**
  - *Pacientes del Día:* Vista de consultas programadas para la fecha actual con accesos rápidos.
  - *Pendiente por Agendar:* Identificación y seguimiento de pacientes inactivos o sin próximas citas programadas.
  - *Sin Valoración:* Control de pacientes de nuevo ingreso o casos especiales que requieren apertura de expediente antropométrico.

### 👥 Gestión de Pacientes y Expedientes
- **Control Completo (CRUD):** Registro de datos demográficos, datos de contacto e identificación.
- **Historial Clínico:** Estructura modular para antecedentes médicos, patologías, alergias y hábitos alimentarios.
- **Filtros Inteligentes:** Buscador avanzado y segmentación automática de pacientes activos e inactivos.

### 📊 Módulo de Valoraciones Antropométricas Avanzadas
- **Formulario Dividido en Pestañas con Validación Interceptada:**
  - *Pestaña 1: Información General* (Datos base de la valoración, peso, estatura, IMC y signos vitales).
  - *Pestaña 2: Medidas Corporales* (Perímetros en cm y Pliegues cutáneos en mm).
  - *Pestaña 3: Composición Corporal y Diagnóstico* (Porcentajes de grasa, masa muscular, agua y diagnóstico nutricional).
- **Mapa Antropométrico Anatómico:** Disposición visual en 3 columnas:
  - *Columna Izquierda (Perímetros):* Cintura, tórax, brazo, cadera, pierna y pantorrilla con cálculo automático de diferencia respecto a la consulta anterior.
  - *Columna Central (Silueta):* Representación gráfica interactiva y compacta mediante mapas de calor corporal.
  - *Columna Derecha (Pliegues):* Bíceps, tríceps, suprailíaco, subescapular y femoral con badges de variación porcentual.
- **Análisis de Tendencias:** Historial evolutivo con comparativas en tiempo real de variaciones de Peso, % de Grasa y Perímetro de Cintura respecto a la consulta inmediata anterior.

### ⚙️ Herramientas de Administración e Importación
- **Carga Masiva (Excel):** Importador robusto de pacientes y valoraciones históricas mediante la librería `openpyxl`.
- **Validador de Disponibilidad:** Algoritmo en backend que previene colisiones o duplicidades en el agendamiento de citas.

---

## Tecnologías Utilizadas

### Backend
- **Python 3.13+** con **Flask** (Microframework web de alta eficiencia)
- **SQLite** (Motor de base de datos relacional ligero y de alto rendimiento)
- **Werkzeug & Jinja2** (Mapeo de rutas y motor de renderizado de plantillas de servidor)
- **openpyxl** (Procesamiento y parseo de archivos Excel)

### Frontend
- **Tailwind CSS** (Framework CSS utilitario para diseño moderno y altamente responsivo)
- **Alpine.js** (Framework JS ultra-ligero para reactividad nativa de UI en componentes interactivos)
- **Vanilla JavaScript** (Lógica de intercepción de submits, validaciones y enmascaramiento)

---

## Estructura de Módulos del Sistema

```text
SistemaPacientes/
├── app/
│   ├── controllers/      # Controladores de dominio (Rutas y lógica de negocio)
│   │   ├── auth.py                  # Autenticación y control de accesos
│   │   ├── pacientes.py             # CRUD de Pacientes e Historias Clínicas
│   │   ├── valoracion_antropometrica.py # Gestión de mediciones, IMC y mapa anatómico
│   │   └── main.py                  # Dashboard y consultas consolidadas
│   ├── models/           # Gestión de consultas SQL y lógica del modelo de datos
│   ├── static/           # Recursos estáticos (JS, CSS, imágenes)
│   ├── templates/        # Vistas estructuradas en Jinja2
│   │   ├── base/                    # Plantilla base unificada (base.html)
│   │   ├── dashboard/               # Tabs del Dashboard clínico
│   │   ├── pacientes/               # Parciales del expediente y listados
│   │   ├── valoraciones/            # Parciales del mapa y formulario por pestañas
│   │   └── components/              # Componentes visuales reutilizables (Body Map, etc.)
│   └── utils/            # Helpers de formateo, validaciones y utilerías comunes
├── docs/                 # Documentación del sistema
├── config.py             # Archivo central de configuración de entornos
└── run.py                # Script de arranque del servidor
```

---

## Instalación y Configuración del Entorno

### Requisitos Previos
- Python 3.13 o superior instalado en el sistema.
- Gestor de paquetes `pip` actualizado.

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tbtkd/SGPN.git
   cd SistemaPacientes
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv .venv
   ```
   - En Windows (cmd):
     ```bash
     .venv\Scripts\activate
     ```
   - En macOS / Linux (bash/zsh):
     ```bash
     source .venv/bin/activate
     ```

3. **Instalar todas las dependencias requeridas:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicializar y poblar la Base de Datos (Opcional):**
   ```bash
   python generate_data.py
   ```

5. **Iniciar el Servidor de Desarrollo:**
   ```bash
   python run.py
   ```
   *El servidor estará disponible en [http://localhost:5000](http://localhost:5000)*

---

## Seguridad y Robustez
- **Validación Defensiva de Entrada:** Validación dual (Frontend interceptado + try/except con flash messaging en Backend).
- **Protección de Sesiones:** Manejo seguro de cookies de sesión cifradas.
- **SQL Injection Prevention:** Parametrización estricta de consultas SQLite.
- **Estabilidad de Plantillas:** Uso de accesos seguros con valores predeterminados (`.get(key, 0)|float(0)`) en el motor Jinja2 para prevenir errores 500 ante datos nulos o inconsistencias.
