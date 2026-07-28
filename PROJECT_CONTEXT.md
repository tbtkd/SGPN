# AI INSTRUCTION: Antes de realizar cualquier modificación al código, lee este archivo para alinearte con las decisiones arquitectónicas, reglas de UI/UX y modelos de datos ya establecidos.

---

# 🧠 Memoria Viva del Proyecto (PROJECT_CONTEXT.md)

Este documento registra el estado actual, historial de logros, reglas estrictas de desarrollo y el backlog del **Sistema de Gestión de Pacientes y Nutrición (SGPN)**.

---

## 📜 Changelog / Historial de Logros

- **Línea Base de Requerimientos (SRS)**: Creación e integración oficial del documento `SRS_REQUIREMENTS.md` detallando Casos de Uso (UC-01 a UC-04), requerimientos de datos de las 6 tablas principales y requerimientos no funcionales (NFRs).
- **Módulo Dashboard**: Implementación de KPIs en tiempo real (crecimiento mensual, valoraciones del mes, promedio diario), pestañas de pacientes del día, pacientes sin valoración reciente y gráfico de actividad.
- **Módulo Pacientes**: Registro completo, expedientes clínicos con pestañas, listados de activos/inactivos y gestión de citas asociadas.
- **Módulo Valoraciones Antropométricas**: 
  - Creación de formulario multipestaña con validación robusta en Backend (`try/except`, mensajes `flash()`).
  - Serialización segura de objetos ORM mediante el método `.to_dict()` para consumo en componentes Alpine.js (`_mapa_antropometrico.html`).
  - Mapa corporal interactivo con comparativas automáticas vs. consulta anterior.
- **Módulo Historial Clínico**: 
  - Integración del modelo ORM `HistorialClinico` con relación 1:1 con `Paciente`.
  - Implementación del método estático `HistorialClinico.actualizar(paciente_id, datos)` para prevenir excepciones `AttributeError`.
- **Módulo Pagos y Agenda**: Control financiero y agendamiento vinculado a pacientes.

---

## 📐 Reglas Fijas de Diseño y Desarrollo

1. **Serialización a JSON**: NUNCA pasar objetos ORM directamente a directivas `|tojson` en plantillas Jinja2 / Alpine.js (`x-data`). Utilizar siempre el método `.to_dict()` definido en el modelo (ej. `{{ valoracion.to_dict()|tojson }}`).
2. **Validación Defensiva**: Todos los controladores deben validar los datos entrantes (`request.form`) dentro de bloques `try/except`, utilizando transacciones seguras (`db.session.commit()` / `db.session.rollback()`) y notificando errores mediante `flash()`.
3. **Ancho de Contenedor UI**: Emplear clases de ancho extendido (`max-w-8xl` o fluidas) en contenedores principales de escritorio para aprovechar el espacio visual.
4. **Organización de Plantillas**: Mantener la estructura modular en `app/templates/` utilizando subcarpetas `tabs/` para pestañas principales y `partials/` para componentes reutilizables o fragmentos incluidos mediante Jinja.
5. **Nomenclatura**: Seguir estrictamente el estándar en español para nombres de modelos, tablas, columnas y rutas (snake_case en bases de datos y Python, kebab-case en URLs).

---

## 📋 Backlog y Próximos Pasos

- [ ] **Fase 1**: Refinamiento y pruebas unitarias automáticas para validación de formularios multipestaña con JavaScript (foco automático y cambio de pestaña en error).
- [ ] **Fase 2**: Exportación de expedientes clínicos y reportes nutricionales en formato PDF.
- [ ] **Fase 3**: Módulo de recordatorios y notificaciones automáticas de citas para pacientes.
- [ ] **Fase 4**: Optimización de índices de base de datos para consultas analíticas de alto volumen.
