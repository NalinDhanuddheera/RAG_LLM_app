import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from indexer import index_pdfs
from query import query_index
import os
from llama_index.core import VectorStoreIndex

# Define the path for temporary PDFs
TEMP_PDF_FOLDER = 'resources/temp_pdfs/'

def upload_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if not files:
        return
    
    if not os.path.exists(TEMP_PDF_FOLDER):
        os.makedirs(TEMP_PDF_FOLDER)
    
    for file in files:
        destination = os.path.join(TEMP_PDF_FOLDER, os.path.basename(file))
        with open(file, 'rb') as f:
            with open(destination, 'wb') as temp_file:
                temp_file.write(f.read())
    
    index = index_pdfs(TEMP_PDF_FOLDER)
    save_index(index)  # Ensure to save the index
    messagebox.showinfo("Info", "Indexing completed")

def query_index_action():
    query_text = query_entry.get()
    if not query_text:
        messagebox.showwarning("Warning", "Query cannot be empty.")
        return
    
    index = load_index()  # Load the index
    results = query_index(index, query_text)
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, "\n".join(results))

# app.py
def load_index():
    # Ensure you use a method that loads an existing index
    return VectorStoreIndex.load('path/to/your/index_file')

def save_index(index):
    # Save the index to a file or database
    pass  # Implement your saving logic here

# Create the main window
root = tk.Tk()
root.title("RAG LLM App")

# Configure the main window
root.geometry("800x600")  # Set a default window size
root.resizable(True, True)  # Allow the window to be resizable

# Main Frame
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Upload PDFs Section
upload_frame = tk.Frame(main_frame)
upload_frame.pack(pady=10)

upload_button = tk.Button(upload_frame, text="Upload PDFs", command=upload_pdfs, font=("Helvetica", 12), bg="#4CAF50", fg="white")
upload_button.pack(pady=10)

# Query Section
query_frame = tk.Frame(main_frame)
query_frame.pack(pady=10)

query_label = tk.Label(query_frame, text="Enter query:", font=("Helvetica", 12))
query_label.pack(pady=5)

query_entry = tk.Entry(query_frame, width=60, font=("Helvetica", 12))
query_entry.pack(pady=5)

query_button = tk.Button(query_frame, text="Query", command=query_index_action, font=("Helvetica", 12), bg="#2196F3", fg="white")
query_button.pack(pady=10)

# Results Display
results_frame = tk.Frame(main_frame)
results_frame.pack(pady=10)

results_label = tk.Label(results_frame, text="Results:", font=("Helvetica", 12))
results_label.pack(pady=5)

results_text = scrolledtext.ScrolledText(results_frame, width=80, height=20, font=("Helvetica", 12))
results_text.pack(pady=10)

root.mainloop()
