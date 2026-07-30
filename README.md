# Sistema de Gestión de Pacientes y Nutrición (SGPN / SistemaPacientes)

Sistema integral de gestión clínica, nutricional y administrativa para profesionales de la salud y nutrición, desarrollado en Python (Flask, SQLAlchemy, SQLite) con una interfaz moderna y responsiva basada en Tailwind CSS y Alpine.js.

---

## 1. Overview del Sistema

- **Descripción**: Plataforma web de escritorio / servidor local diseñada para nutriólogos y clínicas nutricionales. Permite la administración completa de pacientes, agendamiento de citas, control de pagos, valoraciones antropométricas avanzadas (con cálculo automático de IMC, % de grasa corporal, masa muscular, áreas corporales y somatotipo), generación de historiales clínicos y envío de plantillas de mensajes automatizados.
- **Stack Tecnológico**:
  - **Backend**: Python 3.10+, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate.
  - **Base de Datos**: SQLite (almacenamiento persistente seguro en `%LOCALAPPDATA%/SistemaPacientes/sgpn_nutricion.db` en modo ejecutable).
  - **Frontend**: Tailwind CSS, Alpine.js, FontAwesome, SweetAlert2 para modales y alertas.
- **Arquitectura**: Patrón Model-View-Controller (MVC) modular con separación estricta de responsabilidades (SoC), Blueprints por módulo, manejadores de errores globales resilientes y migración automática de esquemas en caliente.

---

## 2. Guía de Instalación y Entorno (Desarrollo)

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. **Clonar o abrir el repositorio**:
   ```bash
   cd C:\test\py\SistemaPacientes
   ```

2. **Crear y activar el entorno virtual (`venv`)**:
   ```bash
   python -m venv venv
   # En Windows (CMD / PowerShell):
   venv\Scripts\activate
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**:
   ```bash
   python run.py
   ```
   La aplicación abrirá automáticamente el navegador predeterminado en `http://127.0.0.1:5000/`.

---

## 3. Guía de Empaquetado Executable

Para compilar el proyecto en un archivo ejecutable independiente (`.exe`) para Windows utilizando PyInstaller:

1. **Verificar que el entorno virtual esté activo y las dependencias instaladas**.
2. **Ejecutar el script de empaquetado**:
   ```bash
   build_exe.bat
   ```
   O bien mediante PyInstaller directamente usando la especificación:
   ```bash
   pyinstaller SistemaPacientes.spec
   ```
3. El archivo ejecutable resultante y su estructura se generarán en la carpeta `dist/`. La base de datos y archivos de usuario se gestionarán de forma persistente en el equipo cliente dentro de `%LOCALAPPDATA%/SistemaPacientes/`.

---

## 4. Diccionario de Datos y Módulos

### Tablas Principales (`SQLite / SQLAlchemy`)
- **`usuarios`**: Gestión de credenciales, roles (`nutriologa`, `administrador`) y datos de acceso.
- **`pacientes`**: Expediente demográfico, datos de contacto, historial médico base y estatus.
- **`citas`**: Registro de consultas agendadas, estatus (Programada, Completada, Cancelada) y notas.
- **`pagos`**: Control de cobros, conceptos y adeudos asociados a las consultas o paquetes.
- **`valoracion_antropometrica`**: Mediciones antropométricas (peso, talla, pliegues cutáneos, perímetros, % grasa, masa magra, agua corporal).
- **`historial_clinico`**: Antecedentes heredofamiliares, patológicos, no patológicos y recordatorio de 24 horas.
- **`plantilla_mensaje`**: Plantillas prediseñadas para recordatorios y seguimiento por WhatsApp/Correo.
- **`bitacora_contacto`**: Registro de comunicaciones y seguimientos realizados al paciente.

### Layout de Carga Masiva (Excel)
El sistema soporta importación masiva de pacientes mediante archivos `.xlsx` conteniendo las columnas obligatorias: `nombre`, `apellido`, `telefono`, `correo`, `fecha_nacimiento`, `genero`.

---

## 5. API / Endpoints Reference

| Ruta HTTP | Método | Módulo | Descripción | Respuesta JSON (AJAX) / Template |
| --- | --- | --- | --- | --- |
| `/` | GET | Main | Dashboard principal con métricas y resumen de citas. | `dashboard/index.html` |
| `/auth/login` | GET, POST | Auth | Autenticación de usuarios en el sistema. | Vista de login / Redirección |
| `/auth/logout` | GET | Auth | Cierre de sesión de usuario actual. | Redirección a login |
| `/usuarios/` | GET | Auth | Listado de usuarios del sistema (solo nutrióloga). | `auth/lista_usuarios.html` |
| `/pacientes/` | GET | Pacientes | Listado y búsqueda avanzada de pacientes. | `pacientes/lista_pacientes.html` |
| `/pacientes/nuevo` | GET, POST | Pacientes | Formulario de registro de nuevo paciente. | Redirección / JSON |
| `/pacientes/<id>` | GET | Pacientes | Expediente detallado y panel lateral de acciones. | `pacientes/detalle_paciente.html` |
| `/historiales/<id>` | GET, POST | Historial | Gestión del historial clínico nutricional. | `historiales/historial_clinico.html` |
| `/valoraciones/<id>` | GET, POST | Valoración | Valoración antropométrica y cálculos corporales. | `valoraciones/detalle_valoracion.html` |
| `/plantillas/` | GET, POST | Plantillas | Administración de plantillas de mensajes. | `plantillas/index.html` |
| `/api/pacientes/<id>/estatus` | POST | API | Actualización dinámica de estatus de paciente. | `{'success': True}` |
