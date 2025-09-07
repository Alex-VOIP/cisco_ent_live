"""A live viewer for a Cisco phone's screen.

This script uses tkinter to create a simple GUI that displays a continuously
updated screenshot from a Cisco IP phone. The refresh interval and the phone's
IP address can be configured within the script.
"""

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
    """A class to display a live view of a Cisco phone's screen."""
    def __init__(self):
        """Initializes the Viewer application.

        This method sets up the main tkinter window, creates a label to display
        the phone's screen, and starts a background thread to fetch screenshots.
        """
        self.root = tk.Tk()
        self.root.title("Cisco Live")
        self.label = tk.Label(self.root)
        self.label.pack()
        self.running = True
        threading.Thread(target=self.loop, daemon=True).start()

    def loop(self):
        """The main loop for fetching and displaying screenshots.

        This method runs in a background thread and continuously fetches new
        screenshots from the Cisco phone. It updates the image displayed in the
        GUI. The loop will terminate when `self.running` is set to False.
        """
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
        """Starts the tkinter main loop.

        This method should be called to start the GUI application. It will block
        until the main window is closed.
        """
        self.root.mainloop()

if __name__ == "__main__":
    Viewer().run()
