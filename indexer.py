from llama_index import Document, SimpleIndex
from pypdf import PdfReader
import os

def index_pdfs(pdf_folder_path: str):
    index = SimpleIndex()
    
    # Loop through all PDF files in the folder
    for file_name in os.listdir(pdf_folder_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(pdf_folder_path, file_name)
            # Read the PDF
            with open(file_path, 'rb') as file:
                pdf = PdfReader(file)
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
                
                # Index the document
                doc = Document(text=text, metadata={"source": file_name})
                index.add_document(doc)

    return index
