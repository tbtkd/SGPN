# Especificación de Requerimientos de Software (SRS) - Sistema de Gestión de Pacientes y Nutrición (SGPN)

## 1. Introducción y Propósito
El **Sistema de Gestión de Pacientes y Nutrición (SGPN)** es una aplicación web desarrollada para optimizar el flujo de trabajo en clínicas nutricionales. Permite la administración integral de pacientes, agendamiento de citas, control de pagos, registro de historiales clínicos y valoraciones antropométricas detalladas con validación avanzada en frontend y backend.

---

## 2. Casos de Uso (UC-01 a UC-04)

### UC-01: Gestión de Pacientes
* **Descripción:** Permite registrar, consultar, actualizar y dar de baja a los pacientes de la clínica.
* **Actor Principal:** Nutrióloga / Administrador.
* **Flujo Principal:**
  1. El usuario accede al módulo de pacientes.
  2. Selecciona registrar nuevo paciente o buscar un paciente existente.
  3. Ingresa datos personales (nombre, apellidos, género, fecha de nacimiento, teléfono, correo, ciudad).
  4. El sistema valida los datos y guarda el registro en la base de datos SQLite.
* **Flujo Alternativo:** Si algún campo obligatorio está vacío o tiene formato inválido, el sistema muestra alertas y previene el guardado.

### UC-02: Agendamiento y Control de Citas
* **Descripción:** Gestión del calendario de citas de los pacientes de la clínica.
* **Actor Principal:** Nutrióloga / Administrador.
* **Flujo Principal:**
  1. El usuario selecciona la fecha y hora para programar una cita asociada a un paciente.
  2. El sistema valida la disponibilidad y registra la cita con estado inicial ("pendiente" o "completada").
  3. Permite actualizar el estado de la cita desde el panel del día.

### UC-03: Registro de Historial Clínico
* **Descripción:** Captura de antecedentes médicos, hábitos de actividad física y pautas nutricionales del paciente.
* **Actor Principal:** Nutrióloga.
* **Flujo Principal:**
  1. El usuario accede al perfil del paciente y selecciona registrar historial clínico.
  2. Completa los campos de cirugías, padecimientos, medicamentos, suplementos, actividad física y hábitos alimenticios.
  3. El sistema valida la información y persiste los datos vinculados al paciente.

### UC-04: Valoración Antropométrica Avanzada
* **Descripción:** Registro estructurado en pestañas de mediciones corporales, plicometría y datos de bioimpedancia con validación defensiva integral.
* **Actor Principal:** Nutrióloga.
* **Flujo Principal:**
  1. El usuario accede a la sección de nueva valoración antropométrica de un paciente.
  2. El formulario presenta 3 pestañas: **Antropométrica**, **Plicometría** y **Datos de Bioimpedancia**.
  3. Al enviar el formulario, el script de JavaScript audita todos los campos requeridos en orden.
  4. Si falta algún campo, cambia automáticamente a la pestaña oculta correspondiente, hace `.focus()` y `scrollIntoView()` en el input con error y despliega un banner visual.
  5. En el Backend (Flask), el controlador valida defensivamente con `request.form`, usa bloques `try/except` para conversión segura y emite mensajes `flash()` en caso de anomalías antes de guardar en SQLite.

---

## 3. Requerimientos de Datos (Modelos y Tablas)

El sistema utiliza **SQLAlchemy ORM** conectado a una base de datos **SQLite** con las siguientes 6 entidades principales:

### 3.1. `usuarios`
* `id` (Integer, Primary Key)
* `username` (String, Unique, Not Null)
* `nombre` (String, Not Null)
* `email` (String, Unique, Not Null)
* `password_hash` (String, Not Null)
* `fecha_creacion` (DateTime)

### 3.2. `pacientes`
* `id` (Integer, Primary Key)
* `nombre` (String, Not Null)
* `apellido_paterno` (String, Not Null)
* `apellido_materno` (String)
* `genero` (String, Not Null)
* `fecha_nacimiento` (Date, Not Null)
* `telefono` (String, Not Null)
* `correo` (String, Not Null)
* `ciudad` (String, Not Null)
* `fecha_registro` (DateTime)

### 3.3. `citas`
* `id` (Integer, Primary Key)
* `paciente_id` (Integer, Foreign Key -> `pacientes.id`, Not Null)
* `fecha` (Date, Not Null)
* `hora` (Time, Not Null)
* `estado` (String, Not Null) -> Valores: `'pendiente'`, `'completada'`, `'cancelada'`

### 3.4. `pagos`
* `id` (Integer, Primary Key)
* `paciente_id` (Integer, Foreign Key -> `pacientes.id`, Not Null)
* `fecha_pago` (Date, Not Null)

### 3.5. `historial_clinico`
* `id` (Integer, Primary Key)
* `paciente_id` (Integer, Foreign Key -> `pacientes.id`, Not Null)
* `cirugias` (Text)
* `padecimientos` (Text)
* `medicamentos` (Text)
* `suplementos` (Text)
* `enfermedades_previas` (Text)
* `enfermedades_actuales` (Text)
* `tipo_actividad_fisica` (String)
* `frecuencia_actividad_fisica` (String)
* `tiempo_actividad_fisica` (String)
* `numero_comidas_diarias` (Integer)
* `alimentos_normales` (Text)
* `alimentos_no_gustados` (Text)
* `fecha_registro` (DateTime)

### 3.6. `valoraciones_antropometricas`
* `id` (Integer, Primary Key)
* `paciente_id` (Integer, Foreign Key -> `pacientes.id`, Not Null)
* `numero_cita` (Integer, Not Null)
* `fecha` (Date, Not Null)
* `estatura` (Float, Not Null)
* `peso` (Float, Not Null)
* `imc` (Float, Not Null)
* `grasa` (Float, Not Null)
* `cintura` (Float, Not Null)
* `torax` (Float, Not Null)
* `brazo` (Float, Not Null)
* `cadera` (Float, Not Null)
* `pierna` (Float, Not Null)
* `pantorrilla` (Float, Not Null)
* `tension_arterial` (String, Not Null)
* `frecuencia_cardiaca` (Integer, Not Null)
* `bicep` (Float, Not Null)
* `tricep` (Float, Not Null)
* `suprailiaco` (Float, Not Null)
* `subescapular` (Float, Not Null)
* `femoral` (Float, Nullable)
* `porcentaje_grasa` (String, Not Null)
* `ultima_dieta` (Text)
* `fecha_registro` (DateTime)

---

## 4. Requerimientos No Funcionales (NFRs)
* **NFR-01 (Seguridad y Defensibilidad):** Validación robusta tanto en el cliente (JavaScript) como en el servidor (Flask con bloques `try/except` y sanitización de tipos).
* **NFR-02 (Usabilidad y Accesibilidad):** Interfaz basada en Tailwind CSS y Alpine.js con navegación intuitiva por pestañas y retroalimentación visual inmediata ante errores de llenado.
* **NFR-03 (Rendimiento):** Tiempos de respuesta menores a 500ms en consultas y transacciones sobre la base de datos SQLite optimizada con SQLAlchemy.
* **NFR-04 (Mantenibilidad):** Arquitectura modular separando controladores, modelos, rutas, servicios y scripts de validación frontend independientes.
