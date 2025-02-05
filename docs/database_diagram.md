# Diagrama de Base de Datos SGPN

## Diagrama Entidad-Relación

[Pacientes] 1 ----< [Valoracion_Antropometrica]
[Pacientes] 1 ----< [Historial_Clinico]
[Pacientes] 1 ----< [Pagos]

## Estructura Detallada

### Tabla: pacientes
┌──────────────────┬─────────────┬─────────┬───────┐
│ Campo            │ Tipo        │ Key     │ Extra │
├──────────────────┼─────────────┼─────────┼───────┤
│ id               │ INTEGER     │ PK      │ AI    │
│ nombre           │ TEXT        │ NOT NULL│       │
│ apellido_paterno │ TEXT        │ NOT NULL│       │
│ apellido_materno │ TEXT        │ NOT NULL│       │
│ fecha_nacimiento │ DATE        │ NOT NULL│       │
│ telefono         │ TEXT        │ NOT NULL│       │
│ correo           │ TEXT        │ UNIQUE  │       │
│ ciudad           │ TEXT        │ NOT NULL│       │
│ fecha_registro   │ TIMESTAMP   │ DEFAULT │ NOW   │
│ status           │ TEXT        │ NOT NULL│       │
└──────────────────┴─────────────┴─────────┴───────┘

### Tabla: valoracion_antropometrica
┌────────────────────┬─────────┬──────────┬───────┐
│ Campo              │ Tipo    │ Key      │ Extra │
├────────────────────┼─────────┼──────────┼───────┤
│ id                 │ INTEGER │ PK       │ AI    │
│ paciente_id        │ INTEGER │ FK       │       │
│ numero_cita        │ INTEGER │ NOT NULL │       │
│ fecha              │ DATE    │ NOT NULL │       │
│ estatura           │ FLOAT   │ NOT NULL │       │
│ peso               │ FLOAT   │ NOT NULL │       │
│ imc                │ FLOAT   │ NOT NULL │       │
│ grasa              │ FLOAT   │ NOT NULL │       │
│ cintura            │ FLOAT   │ NOT NULL │       │
│ torax              │ FLOAT   │ NOT NULL │       │
│ brazo              │ FLOAT   │ NOT NULL │       │
│ cadera             │ FLOAT   │ NOT NULL │       │
│ pierna             │ FLOAT   │ NOT NULL │       │
│ pantorrilla        │ FLOAT   │ NOT NULL │       │
│ tension_arterial   │ TEXT    │ NOT NULL │       │
│ frecuencia_cardiaca│ INTEGER │ NOT NULL │       │
│ bicep              │ FLOAT   │ NOT NULL │       │
│ tricep             │ FLOAT   │ NOT NULL │       │
│ suprailiaco        │ FLOAT   │ NOT NULL │       │
│ subescapular       │ FLOAT   │ NOT NULL │       │
│ femoral            │ FLOAT   │          │       │
│ porcentaje_grasa   │ TEXT    │ NOT NULL │       │
│ ultima_dieta       │ TEXT    │          │       │
└────────────────────┴─────────┴──────────┴───────┘

### Tabla: historial_clinico
┌──────────────────────────┬─────────┬──────────┬───────┐
│ Campo                    │ Tipo    │ Key      │ Extra │
├──────────────────────────┼─────────┼──────────┼───────┤
│ id                       │ INTEGER │ PK       │ AI    │
│ paciente_id              │ INTEGER │ FK       │       │
│ cirugias                 │ TEXT    │          │       │
│ padecimientos            │ TEXT    │          │       │
│ medicamentos             │ TEXT    │          │       │
│ suplementos              │ TEXT    │          │       │
│ enfermedades_previas     │ TEXT    │          │       │
│ enfermedades_actuales    │ TEXT    │          │       │
│ tipo_actividad_fisica    │ TEXT    │          │       │
│ frecuencia_actividad     │ TEXT    │          │       │
│ tiempo_actividad         │ TEXT    │          │       │
│ numero_comidas           │ INTEGER │          │       │
│ alimentos_normales       │ TEXT    │          │       │
│ alimentos_no_gustados    │ TEXT    │          │       │
└──────────────────────────┴─────────┴──────────┴───────┘

### Tabla: pagos
┌────────────┬─────────┬──────────┬───────┐
│ Campo      │ Tipo    │ Key      │ Extra │
├────────────┼─────────┼──────────┼───────┤
│ id         │ INTEGER │ PK       │ AI    │
│ paciente_id│ INTEGER │ FK       │       │
│ fecha_pago │ DATE    │ NOT NULL │       │
└────────────┴─────────┴──────────┴───────┘