import sqlite3
import tkinter as tk
from tkinter import messagebox

DB = "users.db"

def get_conn():
    return sqlite3.connect(DB)

def attempt_login():
    uname = entry_user.get()
    pwd = entry_pass.get()

    # INSECURE: string concatenation -> SQL injection vulnerable
    query = f"SELECT * FROM users WHERE username = '{uname}' AND password = '{pwd}'"
    print("[*] Executing:", query)   # printed to terminal for demo (like screenshot)

    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(query)   # vulnerable!
        row = cur.fetchone()
        if row:
            messagebox.showinfo("Login", f"Login SUCCESS: {row[1]}")
        else:
            messagebox.showwarning("Login", "Login FAILED")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

# ----- GUI -----
root = tk.Tk()
root.title("Secure Login Portal")    # screenshot title
root.geometry("500x320")            # window size similar
root.configure(bg="#eaf3fb")        # light-blue like screenshot

# Header
lbl_head = tk.Label(root, text="Enterprise Login Portal", font=("Helvetica", 20, "bold"), bg="#eaf3fb")
lbl_head.pack(pady=(20,10))

# Username
frm = tk.Frame(root, bg="#eaf3fb")
frm.pack(pady=5)
tk.Label(frm, text="Username", bg="#eaf3fb").pack(anchor="w")
entry_user = tk.Entry(frm, width=40)
entry_user.pack()

# Password
frm2 = tk.Frame(root, bg="#eaf3fb")
frm2.pack(pady=10)
tk.Label(frm2, text="Password", bg="#eaf3fb").pack(anchor="w")
entry_pass = tk.Entry(frm2, show="*", width=40)
entry_pass.pack()

# Login button (with a little visual)
btn = tk.Button(root, text="Login", width=20, height=1, bg="#0b71c9", fg="white", command=attempt_login)
btn.pack(pady=15)

# Footer small text
tk.Label(root, text="Demo App - Intentionally Vulnerable to SQLi", bg="#eaf3fb", fg="gray").pack(side="bottom", pady=8)

root.mainloop()
