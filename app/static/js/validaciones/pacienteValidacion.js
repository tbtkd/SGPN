export function validarFormularioPaciente() {
    const nombre = document.getElementById("nombre").value.trim()
    const apellidoPaterno = document.getElementById("apellido_paterno").value.trim()
    const apellidoMaterno = document.getElementById("apellido_materno").value.trim()
    const fechaNacimiento = document.getElementById("fecha_nacimiento").value
    const telefono = document.getElementById("telefono").value.trim()
    const correo = document.getElementById("correo").value.trim()
    const ciudad = document.getElementById("ciudad").value.trim()
  
    if (
      nombre === "" ||
      apellidoPaterno === "" ||
      apellidoMaterno === "" ||
      fechaNacimiento === "" ||
      telefono === "" ||
      correo === "" ||
      ciudad === ""
    ) {
      mostrarError("Por favor, complete todos los campos.")
      return false
    }
  
    if (!validarFechaNacimiento(fechaNacimiento)) {
      mostrarError("La fecha de nacimiento no es válida.")
      return false
    }
  
    if (!validarTelefono(telefono)) {
      mostrarError("El número de teléfono no es válido. Debe contener solo números y tener 10 dígitos.")
      return false
    }
  
    if (!validarCorreo(correo)) {
      mostrarError("El correo electrónico no es válido.")
      return false
    }
  
    return true
  }
  
  function validarFechaNacimiento(fecha) {
    const hoy = new Date()
    const fechaNacimiento = new Date(fecha)
    return fechaNacimiento < hoy
  }
  
  function validarTelefono(telefono) {
    const regex = /^\d{10}$/
    return regex.test(telefono)
  }
  
  function validarCorreo(correo) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(correo)
  }
  
  function mostrarError(mensaje) {
    alert(mensaje)
  }
  
  