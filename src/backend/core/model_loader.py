# src/backend/core/model_loader.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
from src.backend.utils.logger import setup_logger

# Load variables
load_dotenv()
logger = setup_logger("GeminiLoader")

def init_gemini():
    """Initializes the Gemini model using the API key from .env."""
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        logger.error("❌ GEMINI_API_KEY not found in .env")
        return None
    
    logger.info("🧠 Initializing Google Gemini AI...")
    try:
        genai.configure(api_key=api_key)
        # Using gemini-1.5-flash for speed and low cost
        model = genai.GenerativeModel('gemini-1.5-flash')
        logger.info("✅ Gemini AI initialized successfully.")
        return model
    except Exception as e:
        logger.error(f"❌ Error initializing Gemini: {e}")
        return None

class GeminiWrapper:
    """A wrapper for the Gemini model to provide a .generate interface."""
    def __init__(self, model):
        self.model = model
        
    def generate(self, prompt: str) -> str:
        try:
            logger.info(f"🧪 Sending prompt to Gemini: '{prompt[:50]}...'")
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"❌ Gemini generation error: {e}")
            return f"Error: {e}"

def load_model():
    """Helper to maintain compatible interface."""
    raw_model = init_gemini()
    if raw_model:
        return GeminiWrapper(raw_model)
    return None

if __name__ == "__main__":
    m = load_model()
    if m:
        print("Model Response:", m.generate("Hello, how are you?"))
    else:
        print("Failed to initialize Gemini.")


