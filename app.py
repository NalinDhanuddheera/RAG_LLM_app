import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from indexer import index_pdfs
from query import query_index
import os

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
    messagebox.showinfo("Info", "Indexing completed")

def query_index():
    query_text = query_entry.get()
    if not query_text:
        return
    
    index = load_index()  # Replace with method to load your index
    results = query_index(index, query_text)
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, "\n".join(results))

def load_index():
    # Replace with your method to load the index
    return SimpleIndex()  # Placeholder for actual index loading logic

# Create the main window
root = tk.Tk()
root.title("RAG LLM App")

# Upload PDFs Button
upload_button = tk.Button(root, text="Upload PDFs", command=upload_pdfs)
upload_button.pack(pady=10)

# Query Input
query_label = tk.Label(root, text="Enter query:")
query_label.pack(pady=5)
query_entry = tk.Entry(root, width=50)
query_entry.pack(pady=5)

# Query Button
query_button = tk.Button(root, text="Query", command=query_index)
query_button.pack(pady=10)

# Results Display
results_text = scrolledtext.ScrolledText(root, width=60, height=20)
results_text.pack(pady=10)

root.mainloop()
