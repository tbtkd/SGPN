from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Renderiza la página principal del sistema.
    """
    return render_template('base/index.html')

