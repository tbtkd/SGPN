from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.usuario import Usuario

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # El campo en la BD es 'username', autenticar usuario
        user = Usuario.find_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/registrar-usuario', methods=['GET', 'POST'])
@login_required
def registrar_usuario():
    if current_user.rol != 'nutriologa':
        flash('No tienes permiso para realizar esta acción.', 'error')
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        nombre = request.form.get('nombre')
        apellido_paterno = request.form.get('apellido_paterno')
        apellido_materno = request.form.get('apellido_materno')
        email = request.form.get('email')
        rol = request.form.get('rol')

        if Usuario.create(username, password, nombre, apellido_paterno, apellido_materno, email, rol):
            flash('Usuario registrado exitosamente.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Error al registrar el usuario. Asegúrate de que el usuario o correo no estén duplicados.', 'error')

    return render_template('auth/registrar_usuario.html')
