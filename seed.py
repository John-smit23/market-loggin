from app import app, db, User  # type: ignore
import bcrypt

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all([
        User(first_name='Sarah', last_name='Demo', email='demo@glh.com',
             phone='07700 900001', postcode='M14 5AB', role='customer', marketing=True,
             password_hash=bcrypt.hashpw(b'password123', bcrypt.gensalt()).decode()),
        User(first_name='Admin', last_name='GLH', email='admin@glh.com',
             phone='0161 000 0001', postcode='M1 1AA', role='admin',
             password_hash=bcrypt.hashpw(b'password123', bcrypt.gensalt()).decode()),
    ])
    db.session.commit()
    print('Done. demo@glh.com / admin@glh.com  —  password: password123')
