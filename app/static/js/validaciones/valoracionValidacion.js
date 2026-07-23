/**
 * Valida el formulario de nueva valoración antropométrica.
 * Maneja la navegación entre pestañas de Alpine.js si hay errores.
 * 
 * @param {HTMLFormElement} form - El formulario a validar.
 * @param {Object} alpineData - El objeto de datos de Alpine.js para cambiar de pestaña.
 * @returns {boolean} - Verdadero si es válido, falso de lo contrario.
 */
export function validarFormularioValoracion(form, alpineData) {
    const tabsConfig = {
        'antropometrica': 'Antropométrica',
        'plicometria': 'Plicometría',
        'bioimpedancia': 'Datos de Bioimpedancia'
    };

    const campos = [
        { id: 'numero_cita', label: 'Número de cita', tab: 'antropometrica' },
        { id: 'fecha', label: 'Fecha', tab: 'antropometrica' },
        { id: 'estatura', label: 'Estatura (cm)', tab: 'antropometrica' },
        { id: 'peso', label: 'Peso (kg)', tab: 'antropometrica' },
        { id: 'cintura', label: 'Cintura (cm)', tab: 'antropometrica' },
        { id: 'torax', label: 'Tórax (cm)', tab: 'antropometrica' },
        { id: 'brazo', label: 'Brazo (cm)', tab: 'antropometrica' },
        { id: 'cadera', label: 'Cadera (cm)', tab: 'antropometrica' },
        { id: 'pierna', label: 'Pierna (cm)', tab: 'antropometrica' },
        { id: 'pantorrilla', label: 'Pantorrilla (cm)', tab: 'antropometrica' },
        { id: 'tension_arterial', label: 'Tensión arterial', tab: 'antropometrica' },
        { id: 'frecuencia_cardiaca', label: 'Frecuencia cardíaca (lpm)', tab: 'antropometrica' },
        
        { id: 'bicep', label: 'Bícep (mm)', tab: 'plicometria' },
        { id: 'tricep', label: 'Trícep (mm)', tab: 'plicometria' },
        { id: 'suprailiaco', label: 'Suprailiaco (mm)', tab: 'plicometria' },
        { id: 'subescapular', label: 'Subescapular (mm)', tab: 'plicometria' },
        
        { id: 'grasa', label: 'Grasa (%)', tab: 'bioimpedancia' },
        { id: 'imc', label: 'IMC', tab: 'bioimpedancia' },
        { id: 'porcentaje_grasa', label: 'Grasa Total', tab: 'bioimpedancia' }
    ];

    let primerError = null;

    // Limpiar errores previos y ocultar mensajes inline
    campos.forEach(campo => {
        const el = document.getElementById(campo.id);
        if (el) {
            el.classList.remove('is-invalid');
            
            // Ocultar mensaje inline si existe
            const group = el.closest('.form-group');
            if (group) {
                const errorSpan = group.querySelector('.error-message');
                if (errorSpan) errorSpan.style.display = 'none';
            }

            // Agregar listener para limpiar error al escribir si no existe
            if (!el.dataset.hasErrorListener) {
                el.addEventListener('input', () => {
                    el.classList.remove('is-invalid');
                    if (group) {
                        const errorSpan = group.querySelector('.error-message');
                        if (errorSpan) errorSpan.style.display = 'none';
                    }
                });
                el.dataset.hasErrorListener = 'true';
            }
        }
    });

    // Validar campos de manera secuencial (detenerse y marcar SOLO el primer error encontrado)
    for (const campo of campos) {
        const el = document.getElementById(campo.id);
        if (!el) continue;

        const valor = el.value.trim();
        let esInvalido = false;

        if (valor === "") {
            esInvalido = true;
        } else if (el.type === "number" && (isNaN(valor) || parseFloat(valor) < 0)) {
            esInvalido = true;
        }

        if (esInvalido) {
            primerError = campo;
            
            // Marcar únicamente este campo con error
            el.classList.add('is-invalid');
            
            // Mostrar mensaje inline únicamente para este campo
            const group = el.closest('.form-group');
            if (group) {
                const errorSpan = group.querySelector('.error-message');
                if (errorSpan) errorSpan.style.display = 'block';
            }
            
            // Detener el bucle para no procesar ni marcar los demás campos
            break;
        }
    }

    if (primerError) {
        const nombreTab = tabsConfig[primerError.tab];
        
        // Cambiar a la pestaña del error
        if (alpineData && alpineData.activeTab !== primerError.tab) {
            alpineData.activeTab = primerError.tab;
        }

        // Esperar a que Alpine.js haga la transición y luego dar foco
        setTimeout(() => {
            const el = document.getElementById(primerError.id);
            if (el) {
                el.focus();
                el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }, 150);

        mostrarNotificacion(`Por favor, complete el campo ${primerError.label} en la pestaña ${nombreTab}`, 'error');
        return false;
    }

    // Validar fecha: no futura y no mayor a 10 años atrás
    const fechaEl = document.getElementById('fecha');
    if (fechaEl && fechaEl.value) {
        const fechaIngresada = new Date(fechaEl.value);
        const hoy = new Date();
        
        // Fecha hace 10 años
        const haceDiezAnios = new Date();
        haceDiezAnios.setFullYear(hoy.getFullYear() - 10);

        if (fechaIngresada > hoy) {
            fechaEl.classList.add('is-invalid');
            if (alpineData) alpineData.activeTab = 'antropometrica';
            fechaEl.focus();
            mostrarNotificacion("La fecha de valoración no puede ser futura.", "error");
            return false;
        }
        
        if (fechaIngresada < haceDiezAnios) {
            fechaEl.classList.add('is-invalid');
            if (alpineData) alpineData.activeTab = 'antropometrica';
            fechaEl.focus();
            mostrarNotificacion("La fecha de valoración no puede ser mayor a 10 años atrás.", "error");
            return false;
        }
    }

    // Ocultar banner si todo es válido
    const alertBanner = document.getElementById('validation-alert');
    if (alertBanner) alertBanner.style.display = 'none';

    return true;
}

function mostrarNotificacion(mensaje, tipo) {
    const alertBanner = document.getElementById('validation-alert');
    const alertText = document.getElementById('validation-alert-text');
    
    if (alertBanner && alertText) {
        alertText.textContent = mensaje;
        alertBanner.style.display = 'flex';
        // Desplazar suavemente hasta arriba del formulario para que el usuario lea el banner de error
        alertBanner.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
        alert(mensaje);
    }
}
