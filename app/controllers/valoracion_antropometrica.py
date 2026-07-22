from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.valoracion_antropometrica import ValoracionAntropometrica
from app.models.paciente import Paciente

valoracion = Blueprint('valoracion', __name__, url_prefix='/valoraciones')

# Helpers para conversión segura
def safe_float(val, default=0.0):
    if val is None or str(val).strip() == "":
        return default
    try:
        return float(val)
    except ValueError:
        return default

def safe_int(val, default=0):
    if val is None or str(val).strip() == "":
        return default
    try:
        return int(val)
    except ValueError:
        return default

@valoracion.route('/paciente/<int:paciente_id>/nueva', methods=['GET', 'POST'])
def nueva_valoracion(paciente_id):
    paciente = Paciente.obtener_por_id(paciente_id)
    if not paciente:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))

    if request.method == 'POST':
        # 1. Validar presencia de campos obligatorios mínimos en el Backend
        campos_requeridos = ['numero_cita', 'fecha', 'estatura', 'peso', 'imc', 'grasa']
        for campo in campos_requeridos:
            if not request.form.get(campo):
                flash(f"El campo '{campo.replace('_', ' ').capitalize()}' es obligatorio.", 'error')
                return render_template('valoraciones/nueva_valoracion.html', paciente=paciente)

        # 2. Casteo seguro de tipos
        try:
            datos = {
                'numero_cita': safe_int(request.form['numero_cita']),
                'fecha': request.form['fecha'].strip(),
                'estatura': safe_float(request.form['estatura']),
                'peso': safe_float(request.form['peso']),
                'imc': safe_float(request.form['imc']),
                'grasa': safe_float(request.form['grasa']),
                'cintura': safe_float(request.form.get('cintura')),
                'torax': safe_float(request.form.get('torax')),
                'brazo': safe_float(request.form.get('brazo')),
                'cadera': safe_float(request.form.get('cadera')),
                'pierna': safe_float(request.form.get('pierna')),
                'pantorrilla': safe_float(request.form.get('pantorrilla')),
                'tension_arterial': request.form.get('tension_arterial', '').strip(),
                'frecuencia_cardiaca': safe_int(request.form.get('frecuencia_cardiaca'), None) if request.form.get('frecuencia_cardiaca') else None,
                'bicep': safe_float(request.form.get('bicep')),
                'tricep': safe_float(request.form.get('tricep')),
                'suprailiaco': safe_float(request.form.get('suprailiaco')),
                'subescapular': safe_float(request.form.get('subescapular')),
                'femoral': safe_float(request.form.get('femoral'), None) if request.form.get('femoral') else None,
                'porcentaje_grasa': safe_float(request.form['porcentaje_grasa'])
            }
        except Exception as e:
            flash(f"Error en el formato de los datos numéricos: {str(e)}", 'error')
            return render_template('valoraciones/nueva_valoracion.html', paciente=paciente)

        exito, mensaje = ValoracionAntropometrica.crear(paciente_id, datos)
        if exito:
            flash(mensaje, 'success')
            return redirect(url_for('valoracion.lista_valoraciones', paciente_id=paciente_id))
        else:
            flash(mensaje, 'error')

    return render_template('valoraciones/nueva_valoracion.html', paciente=paciente)

@valoracion.route('/paciente/<int:paciente_id>/lista')
def lista_valoraciones(paciente_id):
    if paciente_id == 0:
        return redirect(url_for('valoracion.todas_valoraciones'))
    
    paciente = Paciente.obtener_por_id(paciente_id)
    if not paciente:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))

    valoraciones = ValoracionAntropometrica.obtener_por_paciente(paciente_id)
    return render_template('valoraciones/lista_valoraciones.html', paciente=paciente, valoraciones=valoraciones)

@valoracion.route('/')
def todas_valoraciones():
    valoraciones = ValoracionAntropometrica.obtener_todas()
    return render_template('valoraciones/todas_valoraciones.html', valoraciones=valoraciones)

@valoracion.route('/valoraciones/<int:valoracion_id>')
def detalle_valoracion(valoracion_id):
    valoracion = ValoracionAntropometrica.obtener_por_id(valoracion_id)
    if not valoracion:
        flash('Valoración no encontrada', 'error')
        return redirect(url_for('valoracion.todas_valoraciones'))
    
    paciente = Paciente.obtener_por_id(valoracion['paciente_id'])
    historial_valoraciones = ValoracionAntropometrica.obtener_por_paciente(valoracion['paciente_id'])
    
    return render_template('valoraciones/detalle_valoracion.html', 
                            valoracion=valoracion, 
                            paciente=paciente,
                            historial_valoraciones=historial_valoraciones)

@valoracion.route('/valoraciones/<int:valoracion_id>/editar', methods=['GET', 'POST'])
def editar_valoracion(valoracion_id):
    valoracion = ValoracionAntropometrica.obtener_por_id(valoracion_id)
    if not valoracion:
        flash('Valoración no encontrada', 'error')
        return redirect(url_for('valoracion.todas_valoraciones'))

    paciente = Paciente.obtener_por_id(valoracion['paciente_id'])

    if request.method == 'POST':
        datos = {
            'fecha': request.form['fecha'],
            'estatura': request.form['estatura'],
            'peso': request.form['peso'],
            'imc': request.form['imc'],
            'grasa': request.form['grasa'],
            'cintura': request.form['cintura'],
            'torax': request.form['torax'],
            'brazo': request.form['brazo'],
            'cadera': request.form['cadera'],
            'pierna': request.form['pierna'],
            'pantorrilla': request.form['pantorrilla'],
            'tension_arterial': request.form['tension_arterial'],
            'frecuencia_cardiaca': request.form['frecuencia_cardiaca'],
            'bicep': request.form['bicep'],
            'tricep': request.form['tricep'],
            'suprailiaco': request.form['suprailiaco'],
            'subescapular': request.form['subescapular'],
            'femoral': request.form.get('femoral', ''),  # Opcional para hombres
            'porcentaje_grasa': request.form['porcentaje_grasa']
        }

        exito, mensaje = ValoracionAntropometrica.actualizar(valoracion_id, datos)
        if exito:
            flash(mensaje, 'success')
            return redirect(url_for('valoracion.detalle_valoracion', valoracion_id=valoracion_id))
        else:
            flash(mensaje, 'error')

    return render_template('valoraciones/editar_valoracion.html', valoracion=valoracion, paciente=paciente)

@valoracion.route('/valoraciones/<int:valoracion_id>/eliminar', methods=['POST'])
def eliminar_valoracion(valoracion_id):
    valoracion = ValoracionAntropometrica.obtener_por_id(valoracion_id)
    if not valoracion:
        flash('Valoración no encontrada', 'error')
        return redirect(url_for('valoracion.todas_valoraciones'))

    exito, mensaje = ValoracionAntropometrica.eliminar(valoracion_id)
    if exito:
        flash(mensaje, 'success')
        return redirect(url_for('valoracion.lista_valoraciones', paciente_id=valoracion['paciente_id']))
    else:
        flash(mensaje, 'error')
        return redirect(url_for('valoracion.detalle_valoracion', valoracion_id=valoracion_id))
