import gradio as gr
from typing import List
from app.document import process_documents, process_webpages
from app.rag.chain import create_rag_chain

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
            gr.Markdown("## Upload Documents")
            file_input = gr.File(
                label="Upload Documents",
                file_count="multiple",
                file_types=[".pdf", ".txt", ".md"]
            )
            process_btn = gr.Button("Process Documents")
            file_status = gr.Textbox(label="File Status")
            
            gr.Markdown("## Add Webpages")
            urls_input = gr.Textbox(
                label="Enter webpage URLs (one per line or comma-separated)",
                placeholder="https://example.com\nhttps://another-example.com\nhttps://third-example.com",
                lines=5
            )
            webpage_btn = gr.Button("Process Webpages")
            webpage_status = gr.Textbox(label="Webpage Status", lines=3)
        
        with gr.Column():
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Ask a question")
            clear = gr.Button("Clear")
    
    # Set up event handlers
    process_btn.click(
        process_documents,
        inputs=[file_input],
        outputs=[file_status]
    )
    
    webpage_btn.click(
        process_webpages,
        inputs=[urls_input],
        outputs=[webpage_status]
    )
    
    msg.submit(
        chat,
        inputs=[msg, chatbot],
        outputs=[chatbot]
    )
    
    clear.click(lambda: None, None, chatbot, queue=False) 