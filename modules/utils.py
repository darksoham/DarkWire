import socket
import pyperclip
import mimetypes

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def copy_to_clipboard(text):
    pyperclip.copy(text)

def detect_file_os(filepath):
    mime = mimetypes.guess_type(filepath)[0]
    if mime:
        if "pdf" in mime:
            return "PDF File"
        elif "image" in mime:
            return "Image File"
        elif "audio" in mime:
            return "Audio File"
        elif "video" in mime:
            return "Video File"
        elif "msword" in mime or "officedocument" in mime:
            return "Office Document"
    return "Unknown / Binary"
