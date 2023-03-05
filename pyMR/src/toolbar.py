import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Toolbar:
    def __init__(self, master, run_callback):
        self.master = master
        self.run_callback = run_callback

        self.toolbar = tk.Frame(master, bg='gray25')

        self.new_file_icon = tk.PhotoImage(width=16, height=16)
        self.new_file_icon.put('black', to=(8,8))
        self.new_file_button = ttk.Button(self.toolbar, image=self.new_file_icon, command=self.new_file)
        self.new_file_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.open_file_icon = tk.PhotoImage(width=16, height=16)
        self.open_file_icon.put('black', to=(8,8))
        self.open_file_button = ttk.Button(self.toolbar, image=self.open_file_icon, command=self.open_file)
        self.open_file_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.save_file_icon = tk.PhotoImage(width=16, height=16)
        self.save_file_icon.put('black', to=(8,8))
        self.save_file_button = ttk.Button(self.toolbar, image=self.save_file_icon, command=self.save_file)
        self.save_file_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.run_icon = tk.PhotoImage(width=16, height=16)
        self.run_icon.put('black', to=(8,8))
        self.run_button = ttk.Button(self.toolbar, image=self.run_icon, command=self.run_callback)
        self.run_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.toolbar.pack(side=tk.TOP, fill=tk.X)

    def new_file(self):
        result = messagebox.askyesno("New File", "Are you sure you want to create a new file? Unsaved changes will be lost.")
        if result:
            self.master.event_generate("<<NewFile>>")

    def open_file(self):
        filetypes = [("All Files", "*.*"), ("Text Files", "*.txt")]
        file_path = filedialog.askopenfilename(filetypes=filetypes)
        if file_path:
            self.master.event_generate("<<OpenFile>>", data=file_path)

    def save_file(self):
        self.master.event_generate("<<SaveFile>>")
