from flask import *
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.secret_key = 'ms-secret-2026'  # change this if rebranding
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ms.db'
db = SQLAlchemy(app)

# user table - stores everyone who registers
class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    first_name    = db.Column(db.String(50))
    last_name     = db.Column(db.String(50))
    email         = db.Column(db.String(150), unique=True)  # no duplicates
    phone         = db.Column(db.String(20))
    postcode      = db.Column(db.String(10))
    password_hash = db.Column(db.String(255))  # never store plain text passwords
    role          = db.Column(db.String(10), default='customer')
    marketing     = db.Column(db.Boolean, default=False)

# creates the tables if they dont exist yet
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fn       = request.form.get('first_name', '').strip()
        ln       = request.form.get('last_name', '').strip()
        email    = request.form.get('email', '').strip().lower()
        phone    = request.form.get('phone', '').strip()
        postcode = request.form.get('postcode', '').strip().upper()
        pw       = request.form.get('password', '')
        pw2      = request.form.get('confirm_password', '')
        errors = []
        if not all([fn, ln, email, phone, postcode, pw]):
            errors.append('Please fill in all required fields.')
        if len(fn) < 2 or len(ln) < 2:
            errors.append('Name must be at least 2 characters.')
        if '@' not in email or '.' not in email.split('@')[-1]:
            errors.append('Please enter a valid email address.')
        if not any(c.isdigit() for c in phone):
            errors.append('Please enter a valid phone number.')
        if len(postcode) < 5:
            errors.append('Please enter a valid postcode.')
        if len(pw) < 8:
            errors.append('Password must be at least 8 characters.')
        if pw != pw2:
            errors.append('Passwords do not match.')
        if not request.form.get('terms'):
            errors.append('You must agree to the Terms and Conditions.')
        if User.query.filter_by(email=email).first():
            errors.append('An account with that email already exists.')
        if errors:
            return render_template('register.html', errors=errors, form=request.form)
        # hash the password using bcrypt before saving to database
        hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
        user = User(first_name=fn, last_name=ln, email=email,
                    phone=phone, postcode=postcode, password_hash=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Account created! Please sign in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', errors=[], form={})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        pw    = request.form.get('password', '')
        user  = User.query.filter_by(email=email).first()
        # check the password against the stored hash
        if user and bcrypt.checkpw(pw.encode(), user.password_hash.encode()):
            session['user_id']   = user.id
            session['user_name'] = user.first_name
            session['role']      = user.role
            if request.form.get('remember'):
                session.permanent = True
            flash(f'Welcome back, {user.first_name}!', 'success')
            return redirect(url_for('home'))
        return render_template('login.html', error='Incorrect email or password.')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been signed out.', 'success')
    return redirect(url_for('login'))

# doesnt actually send an email, just shows a message
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        flash('If that email is registered, a reset link has been sent.', 'success')
        return redirect(url_for('login'))
    return render_template('forgot_password.html')

if __name__ == '__main__':
    app.run(debug=True)
