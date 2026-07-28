import os
import sys
import traceback
import webbrowser
from threading import Timer
from app import create_app

def open_browser(port):
    """Abre el navegador predeterminado en la URL de la aplicación"""
    try:
        webbrowser.open(f'http://127.0.0.1:{port}/')
    except Exception as e:
        print(f"[ADVERTENCIA] No se pudo abrir el navegador automáticamente: {e}")

if __name__ == '__main__':
    try:
        print("========================================================")
        print("   INICIANDO SISTEMA DE GESTION DE PACIENTES Y NUTRICION ")
        print("========================================================")
        
        app = create_app()
        port = int(os.getenv('PORT', 5000))
        
        # Programa la apertura del navegador después de 1.5 segundos
        Timer(1.5, open_browser, args=[port]).start()
        
        print(f"[INFO] Servidor corriendo en http://127.0.0.1:{port}/")
        app.run(
            host='127.0.0.1',
            port=port,
            debug=False,
            use_reloader=False
        )
    except Exception as e:
        print("\n========================================================")
        print(" [ERROR CRITICO] Ocurrio un fallo al iniciar la aplicacion:")
        print("========================================================")
        traceback.print_exc()
        print("\n")
        input("Presiona ENTER para salir...")
