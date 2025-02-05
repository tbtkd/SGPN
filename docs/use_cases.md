# Documento de Casos de Uso - SGPN

## CU-01: Gestión de Pacientes

### CU-01.1: Alta de Paciente
**Actor Principal:** Nutriólogo
**Precondiciones:** N/A
**Flujo Principal:**
1. El usuario selecciona "Nuevo Paciente"
2. El sistema muestra formulario de registro
3. El usuario ingresa:
   - Nombre completo
   - Fecha nacimiento
   - Teléfono (10 dígitos)
   - Correo (único)
   - Ciudad
4. El sistema valida los datos
5. El sistema registra al paciente como "activo"

**Flujos Alternativos:**
- 4a. Datos inválidos: Sistema muestra error
- 4b. Correo duplicado: Sistema notifica

### CU-01.2: Cambio Estado Paciente
**Actor Principal:** Nutriólogo
**Precondiciones:** Paciente registrado
**Flujo Principal:**
1. Usuario selecciona paciente
2. Usuario cambia estado (activo/inactivo)
3. Sistema actualiza estado

## CU-02: Valoraciones Antropométricas

### CU-02.1: Nueva Valoración
**Actor Principal:** Nutriólogo
**Precondiciones:** Paciente activo
**Flujo Principal:**
1. Usuario selecciona "Nueva Valoración"
2. Sistema muestra formulario
3. Usuario ingresa:
   - Medidas corporales
   - Signos vitales
   - Pliegues cutáneos
4. Sistema calcula IMC automáticamente
5. Sistema registra valoración

### CU-02.2: Importar Excel
**Actor Principal:** Nutriólogo
**Precondiciones:** Archivo Excel con formato correcto
**Flujo Principal:**
1. Usuario selecciona "Importar Excel"
2. Usuario carga archivo
3. Sistema valida formato
4. Sistema procesa datos
5. Sistema muestra resultado

## CU-03: Historial Clínico

### CU-03.1: Registro Historial
**Actor Principal:** Nutriólogo
**Precondiciones:** Paciente registrado
**Flujo Principal:**
1. Usuario selecciona "Historial Clínico"
2. Sistema muestra formulario
3. Usuario registra:
   - Antecedentes médicos
   - Medicamentos
   - Actividad física
   - Hábitos alimenticios
4. Sistema guarda información