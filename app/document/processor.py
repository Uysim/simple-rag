from pathlib import Path
from typing import List
from app.document.loader import load_document, split_text, load_webpage, split_documents
from app.core.vectorstore import get_vectorstore

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

def process_webpages(urls_text: str) -> str:
    """Process multiple webpages and add to vector store."""
    if not urls_text.strip():
        return "Please enter at least one valid URL"
    
    # Parse URLs (one per line or comma-separated)
    urls = []
    for line in urls_text.strip().split('\n'):
        line = line.strip()
        if line:
            # Handle comma-separated URLs on the same line
            for url in line.split(','):
                url = url.strip()
                if url and url.startswith(('http://', 'https://')):
                    urls.append(url)
    
    if not urls:
        return "No valid URLs found. Please enter URLs starting with http:// or https://"
    
    try:
        vectorstore = get_vectorstore()
        total_chunks = 0
        processed_urls = []
        failed_urls = []
        
        for url in urls:
            try:
                # Load webpage
                documents = load_webpage(url)
                
                # Split documents into chunks
                chunks = split_documents(documents)
                
                # Add to vector store
                vectorstore.add_texts(
                    texts=chunks,
                    metadatas=[{"source": url, "type": "webpage"} for _ in chunks]
                )
                
                total_chunks += len(chunks)
                processed_urls.append(url)
                
            except Exception as e:
                failed_urls.append(f"{url}: {str(e)}")
        
        # Build result message
        result = f"Processed {len(processed_urls)} webpages successfully! Added {total_chunks} total chunks."
        
        if failed_urls:
            result += f"\n\nFailed URLs:\n" + "\n".join(failed_urls)
        
        return result
    
    except Exception as e:
        return f"Error processing webpages: {str(e)}" 