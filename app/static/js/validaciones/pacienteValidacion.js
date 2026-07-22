export function validarFormularioPaciente() {
  limpiarErrores();

  const nombre = document.getElementById("nombre").value.trim();
  const apellidoPaterno = document.getElementById("apellido_paterno").value.trim();
  const apellidoMaterno = document.getElementById("apellido_materno").value.trim();
  const fechaNacimiento = document.getElementById("fecha_nacimiento").value;
  const telefono = document.getElementById("telefono").value.trim();
  const correo = document.getElementById("correo").value.trim();
  const ciudad = document.getElementById("ciudad").value.trim();

  let esValido = true;

  if (!nombre) { marcarErrorCampo("nombre", "El nombre es obligatorio."); esValido = false; }
  if (!apellidoPaterno) { marcarErrorCampo("apellido_paterno", "El apellido paterno es obligatorio."); esValido = false; }
  if (!apellidoMaterno) { marcarErrorCampo("apellido_materno", "El apellido materno es obligatorio."); esValido = false; }
  if (!ciudad) { marcarErrorCampo("ciudad", "La ciudad es obligatoria."); esValido = false; }

  if (!fechaNacimiento) {
    marcarErrorCampo("fecha_nacimiento", "La fecha de nacimiento es obligatoria.");
    esValido = false;
  } else if (!validarFechaNacimiento(fechaNacimiento)) {
    marcarErrorCampo("fecha_nacimiento", "La fecha de nacimiento debe ser anterior al día de hoy.");
    esValido = false;
  }

  if (!telefono) {
    marcarErrorCampo("telefono", "El teléfono es obligatorio.");
    esValido = false;
  } else if (!validarTelefono(telefono)) {
    marcarErrorCampo("telefono", "Debe contener exactamente 10 dígitos numéricos.");
    esValido = false;
  }

  if (!correo) {
    marcarErrorCampo("correo", "El correo es obligatorio.");
    esValido = false;
  } else if (!validarCorreo(correo)) {
    marcarErrorCampo("correo", "El formato del correo no es válido.");
    esValido = false;
  }

  if (!esValido) {
    mostrarBannerError("Por favor, corrija los campos marcados en rojo antes de enviar.");
  }

  return esValido;
}

function validarFechaNacimiento(fecha) {
  const hoy = new Date();
  const fechaNacimiento = new Date(fecha);
  return fechaNacimiento < hoy;
}

function validarTelefono(telefono) {
  const regex = /^\d{10}$/;
  return regex.test(telefono);
}

function validarCorreo(correo) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(correo);
}

function marcarErrorCampo(idInput, mensaje) {
  const input = document.getElementById(idInput);
  if (input) {
    input.classList.add("input-error"); // Aplica borde rojo definido en tu base.css o _forms.css
    
    // Crear el mensaje debajo del input
    const errorText = document.createElement("small");
    errorText.className = "text-danger error-feedback";
    errorText.style.display = "block";
    errorText.style.marginTop = "0.25rem";
    errorText.innerText = mensaje;
    input.parentNode.appendChild(errorText);
  }
}

function limpiarErrores() {
  document.querySelectorAll(".input-error").forEach(el => el.classList.remove("input-error"));
  document.querySelectorAll(".error-feedback").forEach(el => el.remove());
  const banner = document.getElementById("js-error-banner");
  if (banner) banner.remove();
}

function mostrarBannerError(mensaje) {
  const form = document.querySelector("form");
  if (form) {
    const banner = document.createElement("div");
    banner.id = "js-error-banner";
    banner.className = "alert alert-error"; // Ajusta a la clase CSS de alertas de tu proyecto
    banner.style.marginBottom = "1rem";
    banner.innerText = mensaje;
    form.insertBefore(banner, form.firstChild);
  }
}

