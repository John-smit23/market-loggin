# Millfield Services

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

### Step 6 — Install all packages in one command
```
pip install -r requirements.txt
```
This installs flask, flask-sqlalchemy and bcrypt all at once.

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
Creates two accounts you can log in with:
- Email: `demo@glh.com` Password: `password123`
- Email: `admin@glh.com` Password: `password123`

---

## Add images
Copy your images into the `static/images/` folder with these exact names:
- `main-page-image.jpg` — hero background (large landscape photo)
- `product-1.jpg` — first product (honey)
- `product-2.jpg` — second product (veg box)
- `product-3.jpg` — third product (sourdough)
- `product-4.jpg` — fourth product (eggs)

---

## Common errors and fixes

**`activate` is not recognised**
→ Run this first in PowerShell as administrator:
```
Set-ExecutionPolicy RemoteSigned
```
Then try Step 5 again.

**ModuleNotFoundError: No module named 'flask'**
→ Your virtual environment is not activated. Make sure you see `(.venv)` in the terminal, then run Step 6 again.

**bcrypt install fails**
→ Run this instead:
```
pip install bcrypt --only-binary :all:
```

**Database error / OperationalError**
→ Delete the file `instance/ms.db` if it exists, then run `python app.py` again. It will recreate the database automatically.

**Port 5000 already in use**
→ Close any other terminal that is running Flask, or restart VS Code.
