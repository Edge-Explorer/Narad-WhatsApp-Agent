# Narad WhatsApp Agent (A+ Extreme Upgrade) 📱🤖

**Narad** is a professional, modular AI assistant focused on secure, free-to-use communication via WhatsApp. Powered by **Google Gemini 2.0 Flash**, it includes 7 extreme features designed for high-performance automation without monthly costs.

---

## 🚀 Extreme Upgrade Features (100% Free)

*   🧠 **Smart SQLite Memory**: Persistent conversation history stored locally.
*   🌐 **Free Web Search**: Live search results via DuckDuckGo (no paid API key needed).
*   📄 **Document Intelligence**: Built-in support for reading PDF and DOCX files.
*   🎭 **Professional AI Persona**: Customized "Digital Twin" system prompt for Gemini.
*   🎤 **Voice Command Support**: Ready for Speech-to-Text integration via `voice_listener.py`.
*   📁 **Auto-File Organizer**: Organize any folder on your laptop with a single command.
*   📡 **Official WhatsApp API**: Seamless Twilio integration for production reliability.

---

## 📁 Project Structure

```text
Narad-WhatsApp-Agent/
├── src/
│   ├── backend/
│   │   ├── agents/          # Individual AI agents
│   │   ├── core/            # Gemini Core, Search Tools, & Router
│   │   ├── database/        # Local SQLite Memory management
│   │   ├── scripts/         # Voice listener and automation scripts
│   │   └── utils/           # Shared logging utilities
├── data/                    # PDF/Docx documents for Narad to read
├── main.py                  # CLI Entry point
└── .env                     # App configuration (Gemini & Twilio)
```

---

## ⚡ Quick Usage Examples

- **Smart Chat**: Just type `Hi Narad` (It remembers previous chats).
- **Web Search**: `search: What is the current stock price of Google?`
- **Read Docs**: `read: resume.pdf` (Reads files from the `data/` folder).
- **Organize Files**: `organize: C:\Users\ASUS\Downloads`
- **WhatsApp**: `whatsapp: send "Message" to "+918828296303"`
- **System Stats**: `stats` (Check your laptop's CPU/RAM).

---

## 🔑 Configuration

1.  **Google Gemini**: Add `GEMINI_API_KEY` from AI Studio.
2.  **Twilio**: Add `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and your `TWILIO_PHONE_NUMBER` (Sandbox).

---

Developed with ❤️ as a Secure, A+ Extreme AI Assistant.

