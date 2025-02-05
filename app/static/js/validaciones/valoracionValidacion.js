export function validarFormularioValoracion() {
  const numeroCita = document.getElementById("numero_cita").value.trim()
  const fecha = document.getElementById("fecha").value.trim()
  const estatura = document.getElementById("estatura").value.trim()
  const peso = document.getElementById("peso").value.trim()
  const imc = document.getElementById("imc").value.trim()
  const grasa = document.getElementById("grasa").value.trim()
  const cintura = document.getElementById("cintura").value.trim()
  const torax = document.getElementById("torax").value.trim()
  const brazo = document.getElementById("brazo").value.trim()
  const cadera = document.getElementById("cadera").value.trim()
  const pierna = document.getElementById("pierna").value.trim()
  const pantorrilla = document.getElementById("pantorrilla").value.trim()
  const bicep = document.getElementById("bicep").value.trim()
   /*const tension_arterial = document.getElementById("tension_arterial").value.trim()
  const frecuencia_cardiaca = document.getElementById("frecuencia_cardiaca").value.trim()*/
  const tricep = document.getElementById("tricep").value.trim()
  const suprailiaco = document.getElementById("suprailiaco").value.trim()
  const subescapular = document.getElementById("subescapular").value.trim()
  const femoral = document.getElementById("femoral").value.trim()
 const porcentajeGrasa = document.getElementById("porcentaje_grasa").value.trim()

  if (
    numeroCita === "" ||
    fecha === "" ||
    estatura === "" ||
    peso === "" ||
    imc === "" ||
    grasa === "" ||
    cintura === "" ||
    torax === "" ||
    brazo === "" ||
    cadera === "" ||
    pierna === "" ||
    pantorrilla === "" ||
    /*tension_arterial === "" ||
    frecuencia_cardiaca === "" ||*/
    bicep === "" ||
    tricep === "" ||
    suprailiaco === "" ||
    subescapular === "" ||
    porcentajeGrasa === ""
  ) {
    mostrarError("Por favor, complete todos los campos obligatorios.")
    return false
  }

  if (
    !validarNumeroPositivo(estatura) ||
    !validarNumeroPositivo(peso) ||
    !validarNumeroPositivo(imc) ||
    !validarNumeroPositivo(grasa) ||
    !validarNumeroPositivo(cintura) ||
    !validarNumeroPositivo(torax) ||
    !validarNumeroPositivo(brazo) ||
    !validarNumeroPositivo(cadera) ||
    !validarNumeroPositivo(pierna) ||
    !validarNumeroPositivo(pantorrilla) ||
    /*!validarNumeroPositivo(tension_arterial) ||
    !validarNumeroPositivo(frecuencia_cardiaca) ||*/
    !validarNumeroPositivo(bicep) ||
    !validarNumeroPositivo(tricep) ||
    !validarNumeroPositivo(suprailiaco) ||
    !validarNumeroPositivo(subescapular) ||
    !validarNumeroPositivo(porcentajeGrasa)
    ) {
    mostrarError("Por favor, ingrese valores numéricos positivos para todas las medidas.")
    return false
  }

  if (femoral !== "" && !validarNumeroPositivo(femoral)) {
    mostrarError("Por favor, ingrese un valor numérico positivo para la medida femoral (si aplica).")
    return false
  }

  if (!validarFecha(fecha)) {
    mostrarError("Por favor, ingrese una fecha válida.")
    return false
  }

  return true
}

function validarNumeroPositivo(valor) {
  return !isNaN(valor) && Number.parseFloat(valor) > 0
}

function validarFecha(fecha) {
  const fechaActual = new Date()
  const fechaIngresada = new Date(fecha)
  return fechaIngresada instanceof Date && !isNaN(fechaIngresada) && fechaIngresada <= fechaActual
}

function mostrarError(mensaje) {
  alert(mensaje)
}

