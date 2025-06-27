from typing import List
from langchain.chains import ConversationalRetrievalChain
from app.core.llm import create_llm
from app.core.memory import create_memory
from app.core.vectorstore import get_vectorstore

def create_rag_chain():
    """Create RAG chain with conversation memory."""
    # Initialize LLM
    llm = create_llm()
    
    # Initialize memory
    memory = create_memory()
    
    # Get vector store
    vectorstore = get_vectorstore()
    
    # Create chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        return_source_documents=True
    )
    
    return chain 