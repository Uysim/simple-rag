from pathlib import Path
from typing import List
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.core.config import settings

def load_text_file(file_path: Path) -> str:
    """Load text from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_pdf_file(file_path: Path) -> str:
    """Load text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def load_document(file_path: Path) -> str:
    """Load document based on file extension."""
    if file_path.suffix.lower() == '.pdf':
        return load_pdf_file(file_path)
    elif file_path.suffix.lower() in ['.txt', '.md']:
        return load_text_file(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")

def split_text(text: str) -> List[str]:
    """Split text into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
        length_function=len,
    )
    return text_splitter.split_text(text) 