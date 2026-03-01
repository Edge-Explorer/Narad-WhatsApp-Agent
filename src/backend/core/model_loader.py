# src/backend/core/model_loader.py
import os
from google import genai
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
    
    logger.info("🧠 Initializing modern Google Gemini AI client...")
    try:
        # Using the new Google GenAI SDK
        client = genai.Client(api_key=api_key)
        logger.info("✅ Gemini AI client initialized successfully.")
        return client
    except Exception as e:
        logger.error(f"❌ Error initializing Gemini: {e}")
        return None

class GeminiWrapper:
    """A wrapper for the Gemini model to provide a .generate interface."""
    def __init__(self, client):
        self.client = client
        self.model_id = "gemini-1.5-flash"
        
    def generate(self, prompt: str) -> str:
        try:
            logger.info(f"🧪 Sending prompt to Gemini: '{prompt[:50]}...'")
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"❌ Gemini generation error: {e}")
            return f"Error: {e}"

def load_model():
    """Helper to maintain compatible interface."""
    client = init_gemini()
    if client:
        return GeminiWrapper(client)
    return None

if __name__ == "__main__":
    m = load_model()
    if m:
        print("Model Response:", m.generate("Hello, how are you?"))
    else:
        print("Failed to initialize Gemini.")



