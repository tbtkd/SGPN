from app import create_app
from app.models.paciente import Paciente

app = create_app()
with app.app_context():
    resultados = Paciente.obtener_pendientes_por_agendar()
    if resultados:
        print(f"Keys: {resultados[0].keys()}")
        print(f"First row: {dict(resultados[0])}")
    else:
        print("No resultados")
