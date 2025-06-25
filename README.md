# Simple RAG

A simple RAG (Retrieval-Augmented Generation) application built with LangChain, ChromaDB, and Gradio.

## Features

- Document ingestion from PDF and text files
- Efficient document chunking and embedding
- Interactive chat interface
- Persistent vector store

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
python -m app.ui.interface
```

## Project Structure

```
simple-rag/
├── app/
│   ├── core/               # Core functionality
│   ├── document/           # Document processing
│   ├── rag/               # RAG implementation
│   └── ui/                # Gradio interface
├── data/
│   └── vectorstore/       # ChromaDB storage
```

## Usage

1. Place your documents in the `data/documents` directory
2. Launch the application
3. Select documents to process
4. Start chatting with your documents

## License

MIT 