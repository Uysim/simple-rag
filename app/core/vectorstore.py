from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from app.core.config import settings

def get_vectorstore():
    """Get or create a ChromaDB vectorstore using LangChain."""
    embeddings = OpenAIEmbeddings(
        openai_api_key=settings.openai_api_key,
        model=settings.embedding_model
    )
    
    vectorstore = Chroma(
        persist_directory=str(settings.chroma_persist_directory),
        embedding_function=embeddings,
        collection_name="documents"
    )
    
    return vectorstore
