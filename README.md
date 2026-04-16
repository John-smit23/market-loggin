

### 1. Install Python
- Go to python.org → Downloads → Python 3.12
- Run installer → tick **"Add Python to PATH"** → Install Now



### 3. Open Terminal in VS Code
- Terminal → New Terminal (or Ctrl + `)

### 4. Create a virtual environment
```
python -m venv .venv
```

### 5. Activate it
```
.venv\Scripts\activate
```
You should see `(.venv)` at the start of the terminal line.

### 6. Install packages
```
pip install flask flask-sqlalchemy bcrypt
```

### 7. Run the app
```
python app.py
```



## Common errors

**`.venv\Scripts\activate` is not recognised**
→ Run `Set-ExecutionPolicy RemoteSigned` in PowerShell as admin, then try again.

**Port 5000 already in use**
→ Close any other terminal running Flask, or restart VS Code.

**ModuleNotFoundError: No module named 'flask'**
→ Make sure `.venv` is activated (you should see `(.venv)` in the terminal).

