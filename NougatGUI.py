import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import webbrowser
import urllib.request
import os
import sys

# Function to self-install Nougat if not installed
def install_nougat():
    try:
        subprocess.run(["pip", "show", "nougat-ocr"], check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError:
        subprocess.run(["pip", "install", "--upgrade", "fastapi"])
        subprocess.run(["pip", "install", "nougat-ocr"])

# Function to update Nougat and the GUI app
def update_app():
    try:
        # Update Nougat
        subprocess.run(["pip", "install", "--upgrade", "nougat-ocr"], check=True, stdout=subprocess.PIPE)
        
        # Download the latest version of NougatGUI.py from GitHub
        nougat_gui_url = 'https://raw.githubusercontent.com/sm18lr88/Nougat-GUI/main/NougatGUI.py'
        script_path = os.path.abspath(__file__)  # Get the path of the running script
        urllib.request.urlretrieve(nougat_gui_url, script_path)
        
        # Restart the application
        os.execv(sys.executable, ['python'] + sys.argv)
    except Exception as e:
        print(f"Update failed: {e}")

# Function to open PyTorch download page
def open_pytorch_link(event):
    webbrowser.open_new("https://pytorch.org/get-started/locally/")

# Function to check if PyTorch is installed
def is_pytorch_installed():
    try:
        subprocess.run(["pip", "show", "torch"], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Function to browse PDF files
def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, file_path)

# Function to browse output folder
def browse_output_folder():
    folder_path = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, folder_path)

# Function to execute Nougat CLI command
def run_nougat():
    pdf_path = pdf_entry.get()
    output_dir = output_entry.get()
    
    cmd = ["nougat", pdf_path]
    if output_dir:
        cmd.extend(["-o", output_dir])
    if recompute_var.get():
        cmd.append("--recompute")
    if markdown_var.get():
        cmd.append("--markdown")
    
    subprocess.run(cmd, shell=True)

# Main GUI
install_nougat()

root = tk.Tk()
root.title("Nougat PDF Converter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

if not is_pytorch_installed():
    pytorch_label = tk.Label(root, text="Install PyTorch to improve performance", fg="blue", cursor="hand2")
    pytorch_label.grid(row=0, column=0, sticky=tk.W)
    pytorch_label.bind("<Button-1>", open_pytorch_link)
    ttk.Button(root, text="Update", command=update_app).grid(row=1, column=0, sticky=tk.W)
else:
    ttk.Button(root, text="Update", command=update_app).grid(row=0, column=0, sticky=tk.W)

ttk.Label(frame, text="PDF File:").grid(row=0, column=0, sticky=tk.W)
pdf_entry = ttk.Entry(frame, width=40)
pdf_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))
ttk.Button(frame, text="Browse", command=browse_pdf).grid(row=0, column=2)

ttk.Label(frame, text="Output Folder:").grid(row=1, column=0, sticky=tk.W)
output_entry = ttk.Entry(frame, width=40)
output_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))
ttk.Button(frame, text="Browse", command=browse_output_folder).grid(row=1, column=2)

recompute_var = tk.BooleanVar()
markdown_var = tk.BooleanVar()

ttk.Checkbutton(frame, text="Recompute", variable=recompute_var).grid(row=2, column=0, sticky=tk.W)
ttk.Checkbutton(frame, text="Markdown Compatibility", variable=markdown_var).grid(row=2, column=1, sticky=tk.W)

ttk.Button(frame, text="Run", command=run_nougat).grid(row=3, columnspan=3)

root.mainloop()
