
# 🧠 SQLi-Tk-Lab — Local SQL Injection Learning Lab

**Author:** Sunny Mishra (GitHub: https://github.com/sunnymishra565)  

---

## 🔎 Summary
This is a **local, offline learning lab** that demonstrates SQL Injection (SQLi) using a simple Python + Tkinter desktop login app. The repo contains an intentionally **vulnerable** app and a **secure** fixed version, plus instructions to reproduce and test safely on your local machine.

> ⚠️ **Important:** This project is for educational purposes only. Do **NOT** use these techniques on systems you do not own or have explicit written permission to test.

---

## 📁 Repository contents
- `vulnerable_app_tk.py` — intentionally vulnerable Tkinter login (string-concatenation SQL).  
- `secure_app_tk.py` — fixed version using parameterized queries.  
- `init_db.py` — creates `users.db` (local SQLite) with demo users.  
- `demo/` — screenshots / GIFs (optional) for visual demo.  
- `.gitignore` — excludes local DB, venv and caches.  
- `SECURITY.md` — responsible use guidance.  
- `CONTRIBUTING.md` — contribution guidelines.

---

 # SQL Injection Demo — Local Lab Guide

## 🔹 Step 2: Create a Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install bcrypt
```

---

## 🔹 Step 3: Initialize the Demo Database
This command creates a local SQLite database (`users.db`):

```bash
python init_db.py
```

---

## 🔹 Step 4: Run the Vulnerable GUI App
```bash
python vulnerable_app_tk.py
```

---

## 🔹 Step 5: Run the Secure GUI App (for comparison)
```bash
python secure_app_tk.py
```

---

## 🧪 Demo (Local Testing Only)

### ⚠️ Test These Payloads
> Try these **only** on your **local lab** setup.

#### 🔸 Bypass Password (Comment Injection)
```
Username: admin' --
Password: anything
```
➡️ In the vulnerable app, this will likely bypass the password check.

---

#### 🔸 Always-True Payload
```
Username: ' OR '1'='1
Password: ' OR '1'='1
```
➡️ This makes the WHERE condition always true — demonstrating how SQL injection works.

---

### 🖥️ Observe the Query in Terminal
When you run the app, it prints the executed SQL:
```
[*] Executing: SELECT * FROM users WHERE username = '...' AND password = '...'
```

You’ll see how your input directly affects the SQL query structure.

---

## 🔍 Why the Vulnerable Code Is Insecure

The vulnerable code builds SQL queries by **concatenating raw user input**:

```python
query = f"SELECT * FROM users WHERE username = '{uname}' AND password = '{pwd}'"
cur.execute(query)
```

➡️ This allows attackers to inject SQL syntax and **manipulate the query logic** (bypass authentication, read, or modify data).

---

## ✅ Secure Fix: Use Parameterized Queries

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cur.execute(query, (uname, pwd))
```

➡️ User input is now treated as **data**, not executable SQL code — preventing SQL injection.

---

## 💡 Notes & Best Practices

- **Never** build SQL queries by concatenating user input.
- Prefer ORM libraries or parameterized queries.
- Sanitize and validate input where possible.
- Use least-privilege for database accounts.
- Log queries only in safe environments (avoid logging real credentials).

---

*Made for local lab demos — do not test on systems you don't own or have permission to test.*
