# Narad WhatsApp Agent 📱🤖

**Narad** is a professional, modular AI assistant focused on seamless communication via WhatsApp. This project follows the **Model Context Protocol (MCP)** and is powered by the **Google Gemini 2.0 Flash API** for high-performance, low-latency natural language processing.

---

## 🏆 A+ Grade Features

*   **Modular Architecture**: Clean separation between core logic, agents, and utilities.
*   **Official WhatsApp Support**: Powered by **Twilio's Official API** for production-grade reliability.
*   **Built-in MCP Server**: Exposes its WhatsApp capabilities as tools for other AI assistants.
*   **Professional Logging**: Structured logging for debugging and monitoring.
*   **Gemini 2.0 Flash Integration**: Uses Google's latest model for fast, intelligent command processing.

---

## 📁 Project Structure

```text
Narad-WhatsApp-Agent/
├── src/
│   ├── backend/
│   │   ├── agents/          # WhatsApp Agent logic
│   │   ├── core/            # Gemini API integration & command router
│   │   └── utils/           # Shared utilities (logging)
├── main.py                  # Standard CLI entry point
├── mcp_bridge.py            # MCP Server entry point
└── .env                     # API keys (Gemini, Twilio)
```

---

## 🔑 Configuration & API Keys

### 1. Google Gemini API
-   Get your API key from [Google AI Studio](https://aistudio.google.com/).
-   Add it to `.env` as `GEMINI_API_KEY`.

### 2. Twilio WhatsApp API
-   **Step 1**: Register at [Twilio.com](https://www.twilio.com/).
-   **Step 2**: Copy your `Account SID` and `Auth Token` from the Console.
-   **Step 3**: Join the Sandbox by sending the join code to the provided Twilio number.
-   **Step 4**: Update `.env` with your `Account SID`, `Auth Token`, and Sandbox number.

---

## 🚀 Getting Started

1.  **Clone the Repo**:
    ```bash
    git clone <your-repo-link>
    cd Narad-WhatsApp-Agent
    ```

2.  **Create Virtual Environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the CLI**:
    ```bash
    python main.py
    ```

---

## 🧪 Usage Examples (CLI)

- **Send WhatsApp**: `whatsapp: send "Hello from Narad!" to "+918828296303"`
- **AI Chat**: Just type any query, and Narad's Gemini brain will respond.

---

## 🧠 Tech Stack

*   **Backend**: Python
*   **NLP**: Google Gemini 2.0 Flash
*   **WhatsApp**: Twilio API
*   **Protocol**: Model Context Protocol (MCP)

---

Developed with ❤️ as an "A+ Grade" Narad Agent.





