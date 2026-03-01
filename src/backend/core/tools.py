# src/backend/core/tools.py
import os
import shutil
import platform
import psutil
from duckduckgo_search import DDGS
from PyPDF2 import PdfReader
from docx import Document
from src.backend.utils.logger import setup_logger

logger = setup_logger("NaradTools")

class NaradTools:
    """A collection of 100% free professional tools for Narad."""

    @staticmethod
    def web_search(query: str, max_results: int = 3) -> str:
        """Performs a 100% free web search using DuckDuckGo."""
        logger.info(f"🌐 Searching the web for: {query}...")
        try:
            # Note: Using DDGS context manager from duckduckgo_search/ddgs
            with DDGS() as ddgs:
                # Use 'text' method for results
                results = list(ddgs.text(keywords=query, max_results=max_results))
                if not results:
                    return "No results found."
                
                formatted = [f"[{i+1}] {r['title']}: {r['body']} (Link: {r['href']})" for i, r in enumerate(results)]
                return "\n\n".join(formatted)
        except Exception as e:
            logger.error(f"❌ Search Error: {e}")
            return f"Search Error: {e}"

    @staticmethod
    def read_document(file_path: str) -> str:
        """Reads free text from PDF or DOCX files in the data/ folder."""
        logger.info(f"📄 Reading document: {file_path}")
        if not os.path.exists(file_path):
            return f"❌ File not found: {file_path}"
        
        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext == '.pdf':
                reader = PdfReader(file_path)
                text = " ".join([page.extract_text() for page in reader.pages[:5]]) # Limit to 5 pages
                return text if text else "Could not extract text from PDF."
            
            elif ext == '.docx':
                doc = Document(file_path)
                text = "\n".join([p.text for p in doc.paragraphs])
                return text
            
            return "❌ Unsupported format. (Only .pdf, .docx supported)."
        except Exception as e:
            logger.error(f"❌ Doc Reader Error: {e}")
            return f"Doc Reader Error: {e}"

    @staticmethod
    def organize_folder(dir_path: str):
        """Organizes a folder into sub-directories by file type (e.g., images, docs)."""
        logger.info(f"📁 Organizing folder: {dir_path}")
        if not os.path.isdir(dir_path):
            return f"❌ Invalid directory: {dir_path}"

        extensions = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
            'Archives': ['.zip', '.rar', '.7z'],
            'Executables': ['.exe', '.msi'],
            'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java']
        }

        try:
            for filename in os.listdir(dir_path):
                file_ext = os.path.splitext(filename)[1].lower()
                for folder, exts in extensions.items():
                    if file_ext in exts:
                        dest_folder = os.path.join(dir_path, folder)
                        os.makedirs(dest_folder, exist_ok=True)
                        shutil.move(os.path.join(dir_path, filename), os.path.join(dest_folder, filename))
            return f"✅ Folder '{dir_path}' has been organized!"
        except Exception as e:
            logger.error(f"❌ Folder Organization Error: {e}")
            return f"Error: {e}"

    @staticmethod
    def get_system_stats() -> str:
        """Gets free local system information (CPU, RAM)."""
        try:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            os_info = platform.system() + " " + platform.release()
            return f"🖥️ System Status: {os_info} | CPU: {cpu}% | RAM Usage: {ram}%"
        except Exception as e:
            return f"System Error: {e}"
