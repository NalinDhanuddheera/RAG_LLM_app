from llama_index import SimpleIndex
from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

def query_index(index: SimpleIndex, query: str):
    # Perform the query on the index
    results = index.query(query)
    
    # Optionally, use OpenAI for additional processing
    # For example, you can use OpenAI for text completion or refinement
    
    return results
