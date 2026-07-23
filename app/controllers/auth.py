from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.usuario import Usuario
from app.db import get_db
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        password = request.form.get('password')

        if action == 'register':
            db = get_db()
            try:
                db.execute('INSERT INTO usuarios (username, password_hash) VALUES (?, ?)',
                           (username, generate_password_hash(password)))
                db.commit()
                flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
            except Exception as e:
                flash('Error al registrar usuario (posiblemente ya existe).', 'error')
            return redirect(url_for('auth.login'))

        user = Usuario.find_by_username(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        
        flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
