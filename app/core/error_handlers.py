# app/core/error_handlers.py
import logging
from flask import render_template, jsonify, request

logger = logging.getLogger(__name__)

def register_error_handlers(app):
    
    @app.errorhandler(400)
    def bad_request_error(error):
        mensaje = error.description if hasattr(error, 'description') else "Petición incorrecta."
        if request.path.startswith('/api/') or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': mensaje}), 400
        return render_template('errors/400.html', message=mensaje), 400

    @app.errorhandler(404)
    def not_found_error(error):
        if request.path.startswith('/api/') or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': 'Recurso no encontrado'}), 404
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Error interno del servidor [500]: {error}")
        if request.path.startswith('/api/') or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': 'Error interno del servidor'}), 500
        return render_template('errors/500.html'), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        # Captura cualquier excepción genérica no controlada de Python
        logger.exception("Excepción no controlada detectada en el sistema:")
        if request.path.startswith('/api/') or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': 'Ocurrió un error inesperado'}), 500
        return render_template('errors/500.html'), 500