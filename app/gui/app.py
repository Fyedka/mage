import threading
import tkinter as tk
from charsheet import *


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.cs = CharSheet(self.root)
        self.cs.show()


if __name__ == '__main__':
    app = App()
