# Simple RAG

A simple RAG (Retrieval-Augmented Generation) application built with LangChain, ChromaDB, and Gradio.

## Features

- Document ingestion from PDF and text files
- Webpage ingestion with URL support
- Efficient document chunking and embedding
- Interactive chat interface
- Persistent vector store
- Modular architecture with clear separation of concerns

## Setup

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```bash
cp .env.example .env
```

4. Run the application:
```bash
python main.py
```

## Project Structure

```
simple-rag/
├── app/
│   ├── core/               # Core functionality (config, vectorstore)
│   ├── document/           # Document processing (loader, processor)
│   ├── rag/               # RAG implementation (chain)
│   └── ui/                # Gradio interface
├── data/
│   └── vectorstore/       # ChromaDB storage
```

## Usage

1. Launch the application
2. **Upload Documents**: Select PDF, TXT, or MD files to process
3. **Add Webpages**: Enter URLs (one per line or comma-separated) to ingest web content
4. Start chatting with your documents and webpages

## Architecture

The application follows a modular architecture:

- **UI Layer** (`app/ui/`): Gradio interface components
- **Document Layer** (`app/document/`): Document loading and processing logic
- **RAG Layer** (`app/rag/`): Retrieval-augmented generation implementation
- **Core Layer** (`app/core/`): Configuration and vector store management


## Reference

To understand RAG in the bigger picture checkout my [LinkedIn Post](https://www.linkedin.com/posts/uysim-ty_rag-ai-llm-activity-7181259205654319104-B2s_?utm_source=share&utm_medium=member_desktop&rcm=ACoAABuzUcUBzY84P7Y1wcoqY899Gt4pCLhr_cQ)

## License

MIT 
