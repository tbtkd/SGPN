import os
from flask import Flask
from app.db import init_db
from app.config import config

def create_app(config_name=None):
    """
    Función factory para crear y configurar la aplicación Flask
    Args:
        config_name (str): Nombre de la configuración a utilizar (default, development, production)
    Returns:
        Flask: Aplicación Flask configurada
    """
    # Determinar la configuración a usar
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    # Inicialización de la aplicación Flask
    app = Flask(__name__,
                static_folder='static',
                template_folder='templates') 
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # TODO: Descomentar para ambiente de desarrollo
    # from app.logger import setup_logger
    # setup_logger(app, config[config_name])
    
    # Inicialización de la base de datos
    try:
        with app.app_context():
            init_db()
    except Exception as e:
        raise
    
    # Registro de blueprints
    from app.controllers.main import main as main_blueprint
    from app.controllers.pacientes import pacientes as pacientes_blueprint
    from app.controllers.historial_clinico import historial_clinico as historial_blueprint
    from app.controllers.valoracion_antropometrica import valoracion as valoracion_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(pacientes_blueprint)
    app.register_blueprint(historial_blueprint)
    app.register_blueprint(valoracion_blueprint)
    
    return app