from flask import Blueprint, render_template, request
from datetime import datetime
from app.models.paciente import Paciente
from app.models.valoracion_antropometrica import ValoracionAntropometrica

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Renderiza la página principal del sistema con KPIs y actividad reciente.
    """
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    total_pacientes = Paciente.contar_activos()
    crecimiento_pacientes = Paciente.calcular_crecimiento_mensual()
    valoraciones_mes = ValoracionAntropometrica.contar_mes_vigente()
    
    # Cálculo dinámico del promedio diario
    dia_actual = datetime.now().day
    promedio_diario = round(valoraciones_mes / dia_actual, 1)
    
    pacientes_seguimiento = Paciente.contar_en_seguimiento()
    pacientes_sin_valoracion = Paciente.obtener_sin_valoracion_reciente(dias=30)
    proximos_pacientes = Paciente.obtener_proximos(limite=5)
    
    # Si hay filtro de fechas, obtener actividad filtrada
    if fecha_inicio and fecha_fin:
        actividad_reciente = ValoracionAntropometrica.obtener_por_rango(fecha_inicio, fecha_fin)
    else:
        actividad_reciente = ValoracionAntropometrica.obtener_recientes(limite=10)
    
    return render_template('base/index.html', 
                           total_pacientes=total_pacientes,
                           crecimiento_pacientes=crecimiento_pacientes,
                           valoraciones_mes=valoraciones_mes,
                           promedio_diario=promedio_diario,
                           pacientes_seguimiento=pacientes_seguimiento,
                           pacientes_sin_valoracion=pacientes_sin_valoracion,
                           proximos_pacientes=proximos_pacientes,
                           actividad_reciente=actividad_reciente)

