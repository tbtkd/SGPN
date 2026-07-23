import os
from flask import Flask
from flask_login import LoginManager
from app.db import init_db
from app.config import config
from app.core.error_handlers import register_error_handlers

login_manager = LoginManager()

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
    from app.controllers.auth import auth as auth_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(pacientes_blueprint)
    app.register_blueprint(historial_blueprint)
    app.register_blueprint(valoracion_blueprint)
    app.register_blueprint(auth_blueprint)
    
    # REGISTRO DE MANEJADORES GLOBALES DE ERROR
    register_error_handlers(app)
    
    # CONFIGURACIÓN DE LOGIN
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.usuario import Usuario
        return Usuario.get(user_id)
    
    # FILTROS GLOBALES DE JINJA2
    @app.template_filter('format_date')
    def format_date(value):
        if not value:
            return ""
        try:
            fecha_str = str(value)
            fecha = fecha_str.split('-')
            meses = ["", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
            return f"{fecha[2]} {meses[int(fecha[1])]}, {fecha[0]}"
        except:
            return value
    
    return app
