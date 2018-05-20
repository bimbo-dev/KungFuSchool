from app import app, db
from ..models import User
from werkzeug.security import generate_password_hash


@app.cli.command()
def seed_database():
    print('Seeding...')
    # Seeding the User Table
    admin_user, password = 'admin', 'Password123!'
    if db.session.query(User).scalar() is None:
        print('Seeding User table...')
        user = User(username=admin_user, password_hash=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

    print('Done.')
