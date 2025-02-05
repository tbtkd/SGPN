export function validarFormularioHistorialClinico() {
    const tipoActividad = document.getElementById("tipo_actividad_fisica").value.trim()
    const frecuenciaActividad = document.getElementById("frecuencia_actividad_fisica").value.trim()
    const tiempoActividad = document.getElementById("tiempo_actividad_fisica").value.trim()
    const numeroComidas = document.getElementById("numero_comidas_diarias").value.trim()
    const alimentosNormales = document.getElementById("alimentos_normales").value.trim()
    const alimentosNoGustados = document.getElementById("alimentos_no_gustados").value.trim()
    const cirugias = document.getElementById("cirugias").value.trim()
    const medicamentos = document.getElementById("medicamentos").value.trim()
    const suplementos = document.getElementById("suplementos").value.trim()
    const enfermedadesPrevias = document.getElementById("enfermedades_previas").value.trim()
    const enfermedadesActuales = document.getElementById("enfermedades_actuales").value.trim()
  
    if (
      tipoActividad === "" ||
      frecuenciaActividad === "" ||
      tiempoActividad === "" ||
      numeroComidas === "" ||
      alimentosNormales === "" ||
      alimentosNoGustados === ""
    ) {
      mostrarError("Por favor, complete todos los campos obligatorios.")
      return false
    }
  
    if (!validarNumeroComidas(numeroComidas)) {
      mostrarError("El número de comidas diarias debe ser un número entre 1 y 10.")
      return false
    }
  
    return true
  }
  
  function validarNumeroComidas(numero) {
    const num = Number.parseInt(numero)
    return !isNaN(num) && num >= 1 && num <= 10
  }
  
  function mostrarError(mensaje) {
    alert(mensaje)
  }
  
  