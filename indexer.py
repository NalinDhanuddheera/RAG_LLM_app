from llama_index.core import VectorStoreIndex
from llama_index.llms.openai import OpenAI
from pypdf import PdfReader
import os

def index_pdfs(pdf_folder_path: str):
    # Initialize the OpenAI LLM
    openai_llm = OpenAI()  # Assuming OpenAI is being used as the LLM
    
    # Initialize the vector store index
    index = VectorStoreIndex()

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

                # Create a document
                doc = {
                    'text': text,
                    'metadata': {"source": file_name}
                }

                # Add document to index
                index.add_document(doc)

    return index
