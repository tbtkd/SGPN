# Documentación del Backend (SGPN)

## 1. Arquitectura y Estructura
El backend está desarrollado en **Python (Flask)** utilizando el patrón modular de **Blueprints**. Los controladores gestionan la lógica de negocio, la validación defensiva y la interacción con la base de datos mediante **Flask-SQLAlchemy**.

### Blueprints Principales:
- `auth`: Gestión de autenticación de usuarios (`/login`, `/logout`).
- `dashboard`: Indicadores, pacientes del día y métricas generales.
- `pacientes`: CRUD de pacientes, historial clínico, agendamiento de citas, pagos y bitácora de WhatsApp.
- `valoraciones`: Módulo de valoraciones antropométricas por pestañas con validación defensiva.
- `plantillas`: Gestión y catálogo de plantillas predeterminadas de WhatsApp.

---

## 2. Modelos de Base de Datos y ORM

### 2.1. `PlantillaWhatsApp` (Tabla: `plantillas_whatsapp`)
Permite administrar mensajes predeterminados para el contacto con pacientes.
* **Campos Clave:**
  * `id`: Identificador único (Integer, PK).
  * `titulo`: Título descriptivo de la plantilla (String, Not Null).
  * `contenido`: Cuerpo del mensaje con soporte de variables dinámicas `{nombre}` y `{dias}` (Text, Not Null).
  * `esta_activa`: Booleano que define si es la plantilla predeterminada activa (Boolean, Not Null).
* **Regla de Negocio (Plantilla Activa Única):** Al activar una plantilla, el controlador desactiva automáticamente cualquier otra existente en el sistema.

### 2.2. `BitacoraContacto` (Tabla: `bitacoras_contacto`)
Registra cada interacción o envío de mensaje realizado hacia un paciente.
* **Campos Clave:**
  * `id`: Identificador único (Integer, PK).
  * `paciente_id`: Relación con el paciente destinatario (FK).
  * `usuario_id`: Relación con el usuario/nutrióloga que envía (FK).
  * `mensaje`: Texto final enviado (Text, Not Null).
  * `fecha_envio`: Timestamp automático de la interacción.

### 2.3. Control de Citas (`Cita`)
* **Estados:** `'pendiente'`, `'completada'`, `'cancelada'`.
* **Regla de Cierre Automático:** Al registrar una nueva valoración antropométrica o un historial clínico para el paciente, el sistema busca automáticamente la cita asociada del día con estado `'pendiente'` y la actualiza a `'completada'`, limpiando la vista de "Pacientes del Día" en el Dashboard.

---

## 3. Endpoints API Recientes
- `GET /api/plantilla-activa`: Retorna en formato JSON la plantilla activa configurada.
- `GET /api/plantillas-whatsapp`: Lista completa de plantillas para administración asíncrona.
- `GET /pacientes/disponibilidad_horas?fecha=YYYY-MM-DD`: Retorna las horas ya ocupadas en una fecha específica para bloquear dinámicamente el `<select>` de agendamiento en el frontend.
