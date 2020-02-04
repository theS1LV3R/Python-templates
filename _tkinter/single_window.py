"""A template for tkinter"""

import tkinter as tk

class MainApplication(tk.Frame):
    """The main window"""
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Insert gui elements here

if __name__ == "__main__":
    ROOT = tk.Tk()
    MainApplication(ROOT).pack(side="top", fill="both", expand=True)
    ROOT.mainloop()
