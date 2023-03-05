import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.toolbar import Toolbar
from src.other import SyntaxHighlighting, AutoIndentation

VERSION = "0.1 BETA"

class PyMR:
    def __init__(self, master):
        self.master = master
        master.title(f"pyMR - {VERSION}")
        master.geometry("800x600")
        
        # create toolbar
        toolbar_frame = tk.Frame(master, bg="#1e1e1e")
        toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        toolbar = Toolbar(toolbar_frame, self.run_callback)
        
        # create code editor
        self.editor = tk.Text(master, bg="#282c34", fg="white", insertbackground="white", 
                              undo=True, autoseparators=True, maxundo=-1)
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # add syntax highlighting and auto-indentation
        SyntaxHighlighting(self.editor)
        AutoIndentation(self.editor)
        
        # create command prompt and install button
        self.command_frame = tk.Frame(master, bg="#1e1e1e")
        self.command_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.command_entry = tk.Entry(self.command_frame, bg="#282c34", fg="white", insertbackground="white", 
                                      width=60)
        self.command_entry.pack(side=tk.LEFT, padx=10)

        self.install_button = ttk.Button(self.command_frame, text="Install Package", 
                                          command=self.install_package)
        self.install_button.pack(side=tk.LEFT, padx=10)

    def run_callback(self):
        # get the current text in the editor
        code = self.editor.get("1.0", tk.END)

        # execute the code
        try:
            exec(code)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def install_package(self):
        # get the package name from the command entry
        package_name = self.command_entry.get()

        # execute the pip install command
        try:
            import subprocess
            subprocess.check_call(["pip", "install", package_name])
            messagebox.showinfo("Success", f"{package_name} has been installed!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = PyMR(root)
    root.mainloop()
