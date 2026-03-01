# src/backend/scripts/voice_listener.py
import speech_recognition as sr
from src.backend.utils.logger import setup_logger

logger = setup_logger("VoiceAssistant")

def listen_command():
    """Listens to voice input and converts it to text (100% Free)."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        logger.info("🎤 Listening... Speak now.")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            logger.info("🧠 Processing speech...")
            query = r.recognize_google(audio, language='en-in')
            logger.info(f"✅ User said: {query}")
            return query
        except Exception as e:
            logger.warning("⚠️ Could not recognize speech. Please try again.")
            return None

if __name__ == "__main__":
    # Test Standalone
    cmd = listen_command()
    if cmd:
        print(f"Recognized: {cmd}")
