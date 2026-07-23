from flask import Blueprint, render_template
from app.models.paciente import Paciente
from app.models.valoracion_antropometrica import ValoracionAntropometrica

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Renderiza la página principal del sistema con KPIs y actividad reciente.
    """
    total_pacientes = Paciente.contar_activos()
    valoraciones_mes = ValoracionAntropometrica.contar_mes_vigente()
    pacientes_seguimiento = Paciente.contar_en_seguimiento()
    proximos_pacientes = Paciente.obtener_proximos(limite=5)
    actividad_reciente = ValoracionAntropometrica.obtener_recientes(limite=5)
    
    return render_template('base/index.html', 
                           total_pacientes=total_pacientes,
                           valoraciones_mes=valoraciones_mes,
                           pacientes_seguimiento=pacientes_seguimiento,
                           proximos_pacientes=proximos_pacientes,
                           actividad_reciente=actividad_reciente)

