from app.db import get_db, query_db

class Pago:
    @staticmethod
    def registrar(paciente_id, fecha_pago):
        db = get_db()
        db.execute('INSERT INTO pagos (paciente_id, fecha_pago) VALUES (?, ?)', (paciente_id, fecha_pago))
        db.commit()

    @staticmethod
    def obtener_ultimo_pago(paciente_id):
        return query_db('SELECT fecha_pago FROM pagos WHERE paciente_id = ? ORDER BY fecha_pago DESC LIMIT 1', [paciente_id], one=True)

