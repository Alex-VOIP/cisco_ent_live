import requests
import tkinter as tk
from PIL import Image, ImageTk
import io
import threading
import time
import urllib3

urllib3.disable_warnings()

PHONE_IP = "10.0.0.182"
REFRESH_TIME = 0.5  # seconds

class Viewer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cisco Live")
        self.label = tk.Label(self.root)
        self.label.pack()
        self.running = True
        threading.Thread(target=self.loop, daemon=True).start()
        
    def loop(self):
        while self.running:
            try:
                r = requests.get(f"https://{PHONE_IP}/CGI/Screenshot", 
                               auth=("cisco", "cisco"), verify=False, timeout=5)
                img = ImageTk.PhotoImage(Image.open(io.BytesIO(r.content)))
                self.label.config(image=img)
                self.label.image = img
            except:
                pass
            time.sleep(REFRESH_TIME)
    
    def run(self):
        self.root.mainloop()

Viewer().run()