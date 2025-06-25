from typing import List
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from app.core.config import settings
from app.core.vectorstore import get_vectorstore

def create_rag_chain():
    """Create RAG chain with conversation memory."""
    # Initialize LLM
    llm = ChatOpenAI(
        model_name=settings.model_name,
        temperature=0,
        openai_api_key=settings.openai_api_key
    )
    
    # Initialize memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        return_messages=True
    )
    
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