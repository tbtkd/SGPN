# PROJECT_CONTEXT.md - Memoria Viva del Proyecto SGPN

AI INSTRUCTION: Antes de realizar cualquier modificación al código, lee este archivo para alinearte con las decisiones arquitectónicas, reglas de UI/UX y modelos de datos ya establecidos.

---

## 📋 Changelog / Historial de Logros

1. **Módulo de Pacientes y Detalle**:
   - Creación y gestión de expedientes completos de pacientes.
   - Desacoplamiento de scripts JavaScript a `app/static/js/detalle_paciente.js` para manejo de modales de Excel, Cita y Bitácora WhatsApp.

2. **Formulario de Valoración Antropométrica**:
   - Implementación de navegación por pestañas (Antropometría, Pliegues Cutáneos, Signos Vitales).
   - Validación defensiva en Backend (`try/except`, Flask `flash()`) y en Frontend (`valoracionValidacion.js` con cambio automático de pestaña, `.focus()` en el campo erróneo y estilos visuales de error).

3. **Catálogo de Plantillas de WhatsApp**:
   - CRUD completo de plantillas con soporte para placeholders dinámicos (`{nombre}`, `{dias}`).
   - Selector interactivo de plantilla activa con notificaciones flotantes (Toasts) mediante `plantillas.js`.

4. **Suite de Pruebas Unitarias**:
   - Implementación de pruebas automatizadas con `unittest` en `tests/test_sistema.py` cubriendo modelos de ORM (`Paciente`, `PlantillaMensaje`).

---

## 📐 Reglas Fijas de Diseño y Desarrollo

1. **Estructura de Contenedores UI**: Utilizar siempre contenedores responsivos limpios con Tailwind CSS (`max-w-7xl` o superior según diseño).
2. **JavaScript Desacoplado**: **PROHIBIDO** incluir bloques `<script>` largos dentro de las plantillas Jinja2 `.html`. Todo el código JavaScript debe residir en archivos `.js` modulares dentro de `app/static/js/`.
3. **Validación Defensiva**: Toda operación de escritura en base de datos debe estar protegida con bloques `try/except`, rollback en caso de fallo y mensajes claros mediante `flash()`.
4. **Modelos y ORM**: Mantener la convención de nombres en SQLAlchemy (`__tablename__` en plural, propiedades calculadas como `nombre_completo`).
5. **Pruebas**: Cada nueva funcionalidad crítica debe contar con su correspondiente prueba unitaria en `tests/`.

---

## 📌 Backlog y Próximos Pasos

1. **Fase de Analíticas Avanzadas**: Ampliar los gráficos en el Dashboard principal con tendencias de pérdida/ganancia de peso por paciente a lo largo del tiempo.
2. **Exportación de Reportes PDF**: Generación automática de expedientes clínicos y valoraciones en formato PDF desde el detalle del paciente.
3. **Optimización de Cobertura de Pruebas**: Extender la suite unitaria para cubrir controladores y rutas completas de valoraciones y citas.
