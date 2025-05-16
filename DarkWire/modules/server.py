import os

def start_apache():
    os.system("sudo service apache2 start")

def stop_apache():
    os.system("sudo service apache2 stop")

def get_apache_status():
    status = os.popen("systemctl is-active apache2").read().strip()
    return "Running" if status == "active" else "Stopped"

def start_python_server():
    os.system("xterm -bg black -fg green -T 'DarkWire Server' -e 'cd /var/www/html && python3 -m http.server 80'")
