# RAG LLM App

This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) LLM app using Tkinter for a desktop GUI, Llamaindex for indexing, and OpenAI for querying.

## Setup

1. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

2. Set up environment variables in the `.env` file:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## Features

- **Upload PDFs**: Upload multiple PDF files for indexing.
- **Query**: Enter a query to search the indexed PDFs.
- **Results**: View the results in the application window.

