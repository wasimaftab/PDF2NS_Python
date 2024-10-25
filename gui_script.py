import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from app import process_pdfs  # Import your existing function
import threading
import sys

# Create the main window
root = tk.Tk()
root.title("PDF Processor")
root.geometry("600x500")

# Variables to hold user inputs
folder_path_var = tk.StringVar()
namespace_var = tk.StringVar()

# Function to run the PDF processing in a separate thread
def run_process_pdfs():
    folder_path = folder_path_var.get()
    namespace = namespace_var.get()

    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    if not namespace:
        messagebox.showerror("Error", "Please enter a namespace.")
        return

    # Disable the start button to prevent multiple clicks
    start_button.config(state=tk.DISABLED)

    # Function to run in thread
    def task():
        try:
            # Redirect stdout to the output_text widget
            sys.stdout = RedirectText(output_text)

            # Call your existing function
            process_pdfs(folder_path, namespace)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            # Restore stdout
            sys.stdout = sys.__stdout__
            # Re-enable the start button
            start_button.config(state=tk.NORMAL)

    # Start the thread
    threading.Thread(target=task).start()

# Function to select folder
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)

# Class to redirect stdout to the output_text widget
class RedirectText(object):
    def __init__(self, text_widget):
        self.output = text_widget

    def write(self, string):
        self.output.insert(tk.END, string)
        self.output.see(tk.END)  # Auto-scroll to the end

    def flush(self):
        pass  # This is needed for Python 3 compatibility.

# Create the GUI elements
tk.Label(root, text="Namespace:").pack(pady=5)
tk.Entry(root, textvariable=namespace_var, width=50).pack(pady=5)

tk.Button(root, text="Select PDF Folder", command=select_folder).pack(pady=5)
tk.Entry(root, textvariable=folder_path_var, width=50).pack(pady=5)

start_button = tk.Button(root, text="Start Processing", command=run_process_pdfs)
start_button.pack(pady=10)

output_text = scrolledtext.ScrolledText(root, width=90, height=25)
output_text.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
