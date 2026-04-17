# Millfield Services

---

## MAIN ERROR — if you see ModuleNotFoundError (flask / sqlalchemy / bcrypt)
## Try these in order until one works:

```
pip install flask flask-sqlalchemy bcrypt
```
```
python -m pip install flask flask-sqlalchemy bcrypt
```
```
py -m pip install flask flask-sqlalchemy bcrypt
```
```
pip install --user flask flask-sqlalchemy bcrypt
```
```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org flask flask-sqlalchemy bcrypt
```
```
python -m pip install --upgrade pip
pip install flask flask-sqlalchemy bcrypt
```
```
pip install flask flask-sqlalchemy
pip install bcrypt --only-binary :all:
```
```
python -m pip install -r requirements.txt
```

---

## How to run this project (Windows)

### Step 1 — Install Python
- Go to **python.org** → Downloads → Python 3.12
- Run the installer
- **IMPORTANT: tick "Add Python to PATH"** before clicking Install Now

### Step 2 — Open the project in VS Code
- Open VS Code → File → Open Folder → select this folder

### Step 3 — Open the terminal
- In VS Code: Terminal → New Terminal (or press Ctrl + `)

### Step 4 — Create a virtual environment
```
python -m venv .venv
```

### Step 5 — Activate the virtual environment
```
.venv\Scripts\activate
```
You should see `(.venv)` appear at the start of the terminal line.

### Step 6 — Install all packages
```
pip install flask flask-sqlalchemy bcrypt
```

### Step 7 — Run the app
```
python app.py
```
Open your browser and go to: **http://127.0.0.1:5000**

---

## Add test users (optional)
```
python seed.py
```
- Email: `demo@glh.com` Password: `password123`
- Email: `admin@glh.com` Password: `password123`

---

## Add images
Copy into `static/images/` with these exact names:
- `main-page-image.jpg` — hero background
- `product-1.jpg` — honey
- `product-2.jpg` — veg box
- `product-3.jpg` — sourdough
- `product-4.jpg` — eggs

---

## Other common errors

**`activate` is not recognised**
```
Set-ExecutionPolicy RemoteSigned
```
Run that in PowerShell as administrator, then try again.

**`python` is not recognised — use py instead**
```
py -m venv .venv
py -m pip install flask flask-sqlalchemy bcrypt
py app.py
```

**TemplateNotFound: index.html**
→ Make sure all HTML files are inside a `templates/` folder.

**CSS or images not showing**
→ Make sure `style.css` is inside `static/css/` and images are inside `static/images/`.

**Database error / OperationalError**
→ Delete `instance/ms.db` and run `python app.py` again.

**Port 5000 already in use**
→ Close other terminals or change the port in the last line of app.py:
```python
app.run(debug=True, port=5001)
```
Then go to http://127.0.0.1:5001

**Python version error**
→ Run `python --version` — must say Python 3.x.x
