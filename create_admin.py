from main import app, db, User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        admin = User.query.filter_by(email='admin@example.com').first()
        if not admin:
            admin = User(
                email='admin@example.com',
                username='admin',
                password_hash=generate_password_hash('admin123'),
                role='admin'
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin user created: admin@example.com / admin123")
        else:
            print("Admin user already exists.")

if __name__ == '__main__':
    create_admin()
