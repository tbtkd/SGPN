import os
import webbrowser
from threading import Timer
from app import create_app
from app.controllers.pacientes import registrar_proxima_cita

def open_browser(port):
    """Abre el navegador predeterminado en la URL de la aplicación"""
    webbrowser.open(f'http://127.0.0.1:{port}/')

#app = create_app(os.getenv('FLASK_ENV', 'default'))
app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    
    # Programa la apertura del navegador después de 1.5 segundos
    # para dar tiempo a que Flask inicie
    Timer(1.5, open_browser, args=[port]).start()
    
    # Configuración de desarrollo con auto-recarga
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(
        host='127.0.0.1',
        port=port,
        debug=True,  # Habilita el modo de depuración
        use_reloader=True  # Habilita la recarga automática
        
        #debug=debug_mode,
        #use_reloader=debug_mode,
        #extra_files=[  # Monitorear cambios en archivos estáticos y templates
            #'app/static/css/',
            #'app/static/js/',
            #'app/templates/'
        #]
    )
