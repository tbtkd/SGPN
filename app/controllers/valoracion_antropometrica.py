from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.valoracion_antropometrica import ValoracionAntropometrica
from app.models.paciente import Paciente

valoracion = Blueprint('valoracion', __name__, url_prefix='/valoraciones')

@valoracion.route('/paciente/<int:paciente_id>/nueva', methods=['GET', 'POST'])
def nueva_valoracion(paciente_id):
    paciente = Paciente.obtener_por_id(paciente_id)
    if not paciente:
        flash('Paciente no encontrado', 'error')
        return redirect(url_for('pacientes.lista_pacientes'))

    if request.method == 'POST':
        datos = {
            'numero_cita': request.form['numero_cita'],
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
            'femoral': request.form.get('femoral', ''),
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
