import gradio as gr
from pathlib import Path
from typing import List
from app.document.loader import load_document, split_text
from app.core.vectorstore import get_vectorstore
from app.rag.chain import create_rag_chain

def process_documents(files: List[str]) -> str:
    """Process uploaded documents and add to vector store."""
    vectorstore = get_vectorstore()
    
    for file_path in files:
        # Load and split document
        text = load_document(Path(file_path))
        chunks = split_text(text)
        
        # Add to vector store
        vectorstore.add_texts(
            texts=chunks,
            metadatas=[{"source": file_path} for _ in chunks]
        )
    
    return "Documents processed successfully!"

def chat(message: str, history: List[List[str]]) -> List[List[str]]:
    """Process chat message and return response."""
    chain = create_rag_chain()
    response = chain({"question": message})
    
    # Append the new message-response pair to history
    history.append([message, response["answer"]])
    return history

# Create Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Simple RAG Chat")
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Upload Documents",
                file_count="multiple",
                file_types=[".pdf", ".txt", ".md"]
            )
            process_btn = gr.Button("Process Documents")
            status = gr.Textbox(label="Status")
        
        with gr.Column():
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Ask a question")
            clear = gr.Button("Clear")
    
    # Set up event handlers
    process_btn.click(
        process_documents,
        inputs=[file_input],
        outputs=[status]
    )
    
    msg.submit(
        chat,
        inputs=[msg, chatbot],
        outputs=[chatbot]
    )
    
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch() 