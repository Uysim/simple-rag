from langchain.memory import ConversationBufferMemory

def create_memory():
    """Create and configure conversation memory."""
    return ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        return_messages=True
    ) 