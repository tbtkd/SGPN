from app.db import get_db, query_db
import sqlite3
import logging

logger = logging.getLogger(__name__)

class HistorialClinico:
    @staticmethod
    def obtener_por_paciente_id(paciente_id):
        try:
            return query_db('SELECT * FROM historial_clinico WHERE paciente_id = ?', [paciente_id], one=True)
        except Exception as e:
            logger.error(f"Error al obtener historial para paciente {paciente_id}: {e}")
            return None

    @staticmethod
    def crear(paciente_id, datos):
        db = get_db()
        try:
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
            return True, "Historial clínico creado correctamente"
        except sqlite3.Error as e:
            db.rollback()
            logger.error(f"Error al insertar historial clínico para paciente {paciente_id}: {e}")
            return False, f"Error de base de datos al guardar: {str(e)}"

    @staticmethod
    def actualizar(paciente_id, datos):
        db = get_db()
        try:
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
            return True, "Historial clínico actualizado correctamente"
        except sqlite3.Error as e:
            db.rollback()
            logger.error(f"Error al actualizar historial clínico para paciente {paciente_id}: {e}")
            return False, f"Error de base de datos al actualizar: {str(e)}"

    @staticmethod
    def obtener_todos():
        return query_db('''
            SELECT h.*, p.nombre, p.apellido_paterno, p.apellido_materno
            FROM historial_clinico h
            JOIN pacientes p ON h.paciente_id = p.id
        ''')

