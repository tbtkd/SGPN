import sqlite3
import os
from flask import current_app, g
import logging

logger = logging.getLogger(__name__)

def get_db():
    if 'db' not in g:
        try:
            # Usar variable de entorno para la ruta de la base de datos, default a local
            db_path = os.environ.get('DATABASE_URL', 'pacientes.db')
            g.db = sqlite3.connect(
                db_path,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row
        except sqlite3.Error as e:
            logger.error(f"Error crítico al conectar con la base de datos SQLite: {e}")
            raise e
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        try:
            db.close()
        except sqlite3.Error as e:
            logger.error(f"Error al cerrar la base de datos SQLite: {e}")

def init_db():
    try:
        db = get_db()
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        db.commit()
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos con schema.sql: {e}")
        raise e

def query_db(query, args=(), one=False):
    try:
        cur = get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
    except sqlite3.Error as e:
        logger.error(f"Error al ejecutar query: {query}. Args: {args}. Detalle: {e}")
        raise e
