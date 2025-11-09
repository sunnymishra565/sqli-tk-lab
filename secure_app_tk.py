import sqlite3
import tkinter as tk
from tkinter import messagebox

DB = "users.db"

def get_conn():
    return sqlite3.connect(DB)

def attempt_login_secure():
    uname = entry_user.get()
    pwd = entry_pass.get()

    # SECURE: parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print("[*] Executing parameterized query:", query, "params:", (uname, "****"))

    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(query, (uname, pwd))
        row = cur.fetchone()
        if row:
            messagebox.showinfo("Login", f"Login SUCCESS: {row[1]}")
        else:
            messagebox.showwarning("Login", "Login FAILED")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

root = tk.Tk()
root.title("Secure Login Portal")
root.geometry("500x320")
root.configure(bg="#eaf3fb")

tk.Label(root, text="Enterprise Login Portal", font=("Helvetica", 20, "bold"), bg="#eaf3fb").pack(pady=(20,10))
frm = tk.Frame(root, bg="#eaf3fb"); frm.pack(pady=5)
tk.Label(frm, text="Username", bg="#eaf3fb").pack(anchor="w")
entry_user = tk.Entry(frm, width=40); entry_user.pack()
frm2 = tk.Frame(root, bg="#eaf3fb"); frm2.pack(pady=10)
tk.Label(frm2, text="Password", bg="#eaf3fb").pack(anchor="w")
entry_pass = tk.Entry(frm2, show="*", width=40); entry_pass.pack()
btn = tk.Button(root, text="Login", width=20, height=1, bg="#0b71c9", fg="white", command=attempt_login_secure)
btn.pack(pady=15)
tk.Label(root, text="Demo App - Secure (uses parameterized queries)", bg="#eaf3fb", fg="gray").pack(side="bottom", pady=8)

root.mainloop()
