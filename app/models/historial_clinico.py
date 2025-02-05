from app.db import get_db, query_db

class HistorialClinico:
    @staticmethod
    def obtener_por_paciente_id(paciente_id):
        return query_db('SELECT * FROM historial_clinico WHERE paciente_id = ?', [paciente_id], one=True)

    @staticmethod
    def crear(paciente_id, datos):
        db = get_db()
        db.execute('''
            INSERT INTO historial_clinico (
                paciente_id, cirugias, padecimientos, medicamentos, suplementos,
                enfermedades_previas, enfermedades_actuales, tipo_actividad_fisica,
                frecuencia_actividad_fisica, tiempo_actividad_fisica,
                numero_comidas_diarias, alimentos_normales, alimentos_no_gustados
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            paciente_id, datos['cirugias'], datos['padecimientos'], datos['medicamentos'],
            datos['suplementos'], datos['enfermedades_previas'], datos['enfermedades_actuales'],
            datos['tipo_actividad_fisica'], datos['frecuencia_actividad_fisica'],
            datos['tiempo_actividad_fisica'], datos['numero_comidas_diarias'],
            datos['alimentos_normales'], datos['alimentos_no_gustados']
        ))
        db.commit()

    @staticmethod
    def actualizar(paciente_id, datos):
        db = get_db()
        db.execute('''
            UPDATE historial_clinico SET
                cirugias = ?, padecimientos = ?, medicamentos = ?, suplementos = ?,
                enfermedades_previas = ?, enfermedades_actuales = ?, tipo_actividad_fisica = ?,
                frecuencia_actividad_fisica = ?, tiempo_actividad_fisica = ?,
                numero_comidas_diarias = ?, alimentos_normales = ?, alimentos_no_gustados = ?
            WHERE paciente_id = ?
        ''', (
            datos['cirugias'], datos['padecimientos'], datos['medicamentos'],
            datos['suplementos'], datos['enfermedades_previas'], datos['enfermedades_actuales'],
            datos['tipo_actividad_fisica'], datos['frecuencia_actividad_fisica'],
            datos['tiempo_actividad_fisica'], datos['numero_comidas_diarias'],
            datos['alimentos_normales'], datos['alimentos_no_gustados'], paciente_id
        ))
        db.commit()

    @staticmethod
    def obtener_todos():
        return query_db('''
            SELECT h.*, p.nombre, p.apellido_paterno, p.apellido_materno
            FROM historial_clinico h
            JOIN pacientes p ON h.paciente_id = p.id
        ''')

