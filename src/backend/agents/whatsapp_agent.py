# src/backend/agents/whatsapp_agent.py
import os
import re
from typing import Optional
from twilio.rest import Client
import pywhatkit as kit
from dotenv import load_dotenv
from src.backend.agents.base_agent import BaseAgent

# Load environment variables
load_dotenv()

class WhatsAppAgent(BaseAgent):
    """
    WhatsApp Agent that supports both pywhatkit (WhatsApp Web) 
    and Twilio (Official API).
    """

    def __init__(self, use_twilio: bool = False):
        super().__init__("WhatsAppAgent")
        self.use_twilio = use_twilio
        
        # Load keys for Twilio
        self.twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_from = os.getenv("TWILIO_PHONE_NUMBER")

    def _send_with_pywhatkit(self, to: str, message: str) -> str:
        """Sends a message using pywhatkit (local browser needed)."""
        self.logger.info(f"📤 Sending via PyWhatKit to {to}...")
        try:
            # wait_time is 15s to ensure WhatsApp Web loads properly
            kit.sendwhatmsg_instantly(to, message, wait_time=15, tab_close=True, close_time=4)
            return f"✅ WhatsApp message sent via PyWhatKit to {to}!"
        except Exception as e:
            self.logger.error(f"❌ PyWhatKit Error: {e}")
            return f"❌ Failed to send via PyWhatKit: {e}"

    def _send_with_twilio(self, to: str, message: str) -> str:
        """Sends a message using Twilio API (no browser needed)."""
        if not self.twilio_sid or not self.twilio_token:
            return "❌ Twilio credentials missing in .env!"
        
        self.logger.info(f"📡 Sending via Twilio API to {to}...")
        try:
            client = Client(self.twilio_sid, self.twilio_token)
            sent_msg = client.messages.create(
                from_=self.twilio_from,
                body=message,
                to=f"whatsapp:{to}" if not to.startswith("whatsapp:") else to
            )
            return f"✅ WhatsApp message sent via Twilio SID: {sent_msg.sid}"
        except Exception as e:
            self.logger.error(f"❌ Twilio Error: {e}")
            return f"❌ Twilio API Error: {e}"

    def run(self, command: str) -> str:
        """
        Parses the command: whatsapp: send "Hello!" to +1234567890
        """
        self.logger.info(f"📩 Processing command: {command}")
        
        # Regular expression for parsing the command
        match = re.search(r'send\s+["\'](.*?)["\']\s+to\s+["\']?(.*?)["\']?$', command, re.IGNORE_CASE)
        
        if not match:
            return '⚠️ Invalid format! Use: whatsapp: send "Message" to "+1234567890"'
        
        message, to_number = match.groups()
        
        if self.use_twilio:
            return self._send_with_twilio(to_number.strip(), message)
        else:
            return self._send_with_pywhatkit(to_number.strip(), message)

if __name__ == "__main__":
    # Test Standalone
    agent = WhatsAppAgent()
    print(agent.run('send "Testing Narad Upgrade!" to "+919768817033"'))

