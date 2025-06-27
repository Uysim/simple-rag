from langchain.chat_models import ChatOpenAI
from app.core.config import settings

def create_llm():
    """Create and configure the language model."""
    return ChatOpenAI(
        model_name=settings.model_name,
        temperature=0,
        openai_api_key=settings.openai_api_key
    ) 