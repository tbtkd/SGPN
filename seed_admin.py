import sys
from app import create_app, db_orm
from app.models.usuario import Usuario
from werkzeug.security import generate_password_hash

def seed_admin():
    try:
        # Asegurarse de que el contexto de la aplicación esté activo
        app = create_app()
        with app.app_context():
            db_orm.create_all()
            
            # Verificar si ya existe el usuario 'aaur' o 'aaur@sistema.local'
            admin_existente = Usuario.query.filter(
                (Usuario.email == 'aaur@sistema.local') | (Usuario.username == 'aaur')
            ).first()

            if admin_existente:
                print("[INFO] El usuario administrador 'aaur' ya existe en la base de datos.")
                return

            nuevo_admin = Usuario(
                username="aaur",
                email="aaur@sistema.local",
                nombre="Aurora",
                apellido_paterno="Angeles",
                apellido_materno="R",
                password_hash=generate_password_hash("admin123"),
                rol="nutriologa",
                status="activo"
            )
            db_orm.session.add(nuevo_admin)
            db_orm.session.commit()
            print("[ÉXITO] ¡Usuario Administrador 'aaur' creado/verificado correctamente!")
            print("        Usuario / Password: aaur / admin123")
    except Exception as e:
        db_orm.session.rollback()
        print(f"[ERROR] Ocurrió un error al crear el usuario administrador: {e}")

if __name__ == "__main__":
    seed_admin()
