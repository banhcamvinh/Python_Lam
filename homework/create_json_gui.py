import json
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

current_dir = Path(__file__).parent
output_file = current_dir / "data.json"


def on_start():
    if not output_file.exists():
        with open(output_file, "w") as f:
            json.dump([], f)
        status_label.config(text=f"Created: {output_file.name}", fg="green")
        messagebox.showinfo("Done", f"data.json created at:\n{output_file}")
    else:
        status_label.config(text="File already exists.", fg="orange")
        messagebox.showwarning("Already Exists", f"data.json already exists at:\n{output_file}")


root = tk.Tk()
root.title("JSON Creator")
root.geometry("300x150")
root.resizable(False, False)

tk.Label(root, text="Press Start to create data.json", pady=10).pack()

tk.Button(root, text="Start", command=on_start, width=15, height=2, bg="#4CAF50", fg="white").pack()

status_label = tk.Label(root, text="", pady=8)
status_label.pack()

root.mainloop()
