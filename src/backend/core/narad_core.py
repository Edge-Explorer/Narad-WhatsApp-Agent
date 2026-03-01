# src/backend/core/narad_core.py
import os
import sys
from typing import Optional
from src.backend.core.model_loader import load_model
from src.backend.agents.whatsapp_agent import WhatsAppAgent
from src.backend.utils.logger import setup_logger

# Setup Logger
logger = setup_logger("NaradCore")

# Placeholder stubs for separate projects
class GitHubAgent:
    def run(self, command: str) -> str:
        return "⚠️ GitHub Agent is not installed in this core. (Separate project)"

class EmailAgent:
    def run(self, command: str) -> str:
        return "⚠️ Email Agent is not installed in this core. (Separate project)"

def route_command(command: str, model) -> str:
    """
    Routes the user command to the appropriate agent.
    Supported prefixes: github:, email:, whatsapp:
    """
    lower_command = command.lower().strip()

    if lower_command.startswith("github:"):
        gh_command = command[len("github:"):].strip()
        return GitHubAgent().run(gh_command)

    elif lower_command.startswith("email:"):
        email_command = command[len("email:"):].strip()
        return EmailAgent().run(email_command)

    elif lower_command.startswith("whatsapp:"):
        wa_command = command[len("whatsapp:"):].strip()
        # Set use_twilio=True for professional API support
        agent = WhatsAppAgent(use_twilio=True)
        return agent.run(wa_command)


    # Brain: Fallback to Gemini LLM
    logger.info("🧠 Passing to Gemini API...")
    try:
        if model:
            return model.generate(command)
        return "⚠️ Brain not initialized. Please check GEMINI_API_KEY in .env."
    except Exception as e:
        logger.error(f"❌ Gemini Generation Error: {e}")
        return f"❌ Brain Error: {e}"

def start_narad():
    """Main CLI Interface."""
    logger.info("🟢 Starting Narad Base Core...")
    
    model = None
    try:
        model = load_model()
        if model:
            logger.info("✅ Narad Brain (Gemini) ready.")
        else:
            logger.warning("⚠️ Could not initialize Gemini Brain (Check .env).")
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")

    print("\n--- Narad Multi-Agent Assistant (Powered by Gemini) ---")
    print("Commands: 'whatsapp: ...', 'github: ...', 'email: ...'")
    print("Type 'exit' to quit.\n")

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




