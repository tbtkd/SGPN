import os
import sys
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config
from app.core.error_handlers import register_error_handlers

# Renombramos la instancia de SQLAlchemy para evitar conflicto con app.db
db_orm = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def get_base_path():
    if getattr(sys, 'frozen', False):
        # Si corre como ejecutable empaquetado por PyInstaller
        return sys._MEIPASS
    # Si corre en modo desarrollo
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

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
    
    base_path = get_base_path()
    
    if getattr(sys, 'frozen', False):
        # En ejecutable PyInstaller, las carpetas se añadieron como app/templates y app/static
        template_dir = os.path.join(base_path, 'app', 'templates')
        static_dir = os.path.join(base_path, 'app', 'static')
    else:
        # En desarrollo
        template_dir = os.path.join(base_path, 'app', 'templates')
        static_dir = os.path.join(base_path, 'app', 'static')

    # Inicialización de la aplicación Flask
    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=template_dir) 
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Configuración de base de datos persistente para ejecutable o desarrollo
    if getattr(sys, 'frozen', False):
        # Si corre como ejecutable, la BD se guarda en la carpeta donde está el .exe
        exe_dir = os.path.dirname(sys.executable)
        instance_dir = os.path.join(exe_dir, 'instance')
        os.makedirs(instance_dir, exist_ok=True)
        db_path = os.path.join(instance_dir, 'sgpn_nutricion.db')
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    else:
        # En desarrollo, usar la ruta estándar dentro del proyecto
        instance_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
        os.makedirs(instance_dir, exist_ok=True)
        db_path = os.path.join(instance_dir, 'sgpn_nutricion.db')
        if 'SQLALCHEMY_DATABASE_URI' not in app.config:
            app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

    # Inicialización de la base de datos
    db_orm.init_app(app)
    migrate.init_app(app, db_orm)
    
    # Registro de blueprints
    from app.controllers.main import main as main_blueprint
    from app.controllers.pacientes import pacientes as pacientes_blueprint
    from app.controllers.historial_clinico import historial_clinico as historial_blueprint
    from app.controllers.valoracion_antropometrica import valoracion as valoracion_blueprint
    from app.controllers.auth import auth as auth_blueprint
    from app.controllers.plantillas import plantillas_bp as plantillas_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(plantillas_blueprint)
    app.register_blueprint(pacientes_blueprint)
    app.register_blueprint(historial_blueprint)
    app.register_blueprint(valoracion_blueprint)
    app.register_blueprint(auth_blueprint)
    
    # REGISTRO DE MANEJADORES GLOBALES DE ERROR
    register_error_handlers(app)
    
    # CONFIGURACIÓN DE LOGIN
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = None
    
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.usuario import Usuario
        return Usuario.get(user_id)
    
    # CREACIÓN AUTOMÁTICA DE TABLAS SI NO EXISTEN
    with app.app_context():
        from app.models.paciente import Paciente
        from app.models.cita import Cita
        from app.models.pago import Pago
        from app.models.historial_clinico import HistorialClinico
        from app.models.valoracion_antropometrica import ValoracionAntropometrica
        from app.models.usuario import Usuario
        from app.models.plantilla import PlantillaMensaje
        from app.models.bitacora import BitacoraContacto
        
        db_orm.create_all()

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
