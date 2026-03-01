# src/backend/core/narad_core.py
import os
import sys
from typing import Optional
from src.backend.core.model_loader import load_model
from src.backend.agents.whatsapp_agent import WhatsAppAgent
from src.backend.database.memory import MemoryManager
from src.backend.core.tools import NaradTools
from src.backend.utils.logger import setup_logger

# Setup Logger and Memory
logger = setup_logger("NaradCore")
memory = MemoryManager()

def route_command(command: str, model) -> str:
    """Routes the user command to the WhatsApp agent, Free Tools, or Gemini Brain."""
    lower_command = command.lower().strip()

    # 1. Official WhatsApp Tool
    if lower_command.startswith("whatsapp:"):
        wa_command = command[len("whatsapp:"):].strip()
        agent = WhatsAppAgent(use_twilio=True)
        return agent.run(wa_command)

    # 2. Free Web Search Tool
    elif lower_command.startswith("search:"):
        query = command[len("search:"):].strip()
        return NaradTools.web_search(query)

    # 3. Free System Stats Tool
    elif lower_command.startswith("stats:") or lower_command == "stats":
        return NaradTools.get_system_stats()

    # 4. Free Document Reader Tool
    elif lower_command.startswith("read:"):
        file_path = command[len("read:"):].strip()
        # Ensure it looks in the data/ folder by default for safety
        full_path = f"data/{file_path}" if not os.path.exists(file_path) else file_path
        return NaradTools.read_document(full_path)

    # 5. Free Folder Organizer Tool
    elif lower_command.startswith("organize:"):
        folder_path = command[len("organize:"):].strip()
        return NaradTools.organize_folder(folder_path)

    # 6. Brain (Gemini) with SQLite Memory Context
    logger.info("🧠 Passing to Gemini API with Memory...")
    try:
        if model:
            # 100% Free Memory Integration
            context = memory.get_context(limit=5)
            
            # Professional Persona (No extra cost)
            persona = (
                "You are Narad, Karan's Digital Twin and A+ Grade AI Assistant. "
                "You are intelligent, secure, and professional. "
                "Use the following memory of our previous chat if relevant:\n"
                f"{context}\n\n"
                f"Current Request: {command}"
            )
            
            response = model.generate(persona)
            
            # Save the exchange for 100% Free persistence
            memory.save_message("User", command)
            memory.save_message("Narad", response)
            
            return response
            
        return "⚠️ Brain not initialized. Please check GEMINI_API_KEY in .env."
    except Exception as e:
        logger.error(f"❌ Gemini Generation Error: {e}")
        return f"❌ Brain Error: {e}"

def start_narad():
    """Main CLI Interface."""
    logger.info("🟢 Starting Narad Base Core (A+ Grade)...")
    
    model = None
    try:
        model = load_model()
        if model:
            logger.info("✅ Narad Brain (Gemini) ready.")
        else:
            logger.warning("⚠️ Could not initialize Gemini Brain (Check .env).")
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")

    print("\n--- Narad WhatsApp Agent (A+ Extreme Upgrade) ---")
    print("Commands:")
    print("- Chat: Just type anything (Uses Gemini + SQLite Memory)")
    print("- WhatsApp: 'whatsapp: send \"Msg\" to \"+Num\"'")
    print("- Search: 'search: [query]' (100% Free Web Search)")
    print("- Docs: 'read: [filename]' (PDF/Docx in data/ folder)")
    print("- Stats: 'stats' (Check System CPU/RAM)")
    print("- Organize: 'organize: [folder_path]' (Sort files)")
    print("- Exit: 'exit' to quit.\n")

    while True:
        try:
            user_input = input("User ➜ ").strip()
            if user_input.lower() in ["exit", "quit"]:
                logger.info("👋 Shutting down...")
                break
            
            if not user_input:
                continue
                
            response = route_command(user_input, model)
            print(f"Narad ➜ {response}\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"❌ Core process error: {e}")

if __name__ == "__main__":
    start_narad()





