# Narad WhatsApp Agent 📱🤖

**Narad** is a professional, modular AI agent ecosystem designed for seamless communication via WhatsApp, GitHub, and Email. This project follows the **Model Context Protocol (MCP)** and is powered by the **Google Gemini API** for high-performance, low-latency natural language processing without taxing your local machine.

---

## 🏆 A+ Grade Features

*   **Modular Architecture**: Clean separation between core logic, agents, and utilities.
*   **Dual WhatsApp Support**: Use `pywhatkit` for local automation or **Twilio's Official API** for production reliability.
*   **Built-in MCP Server**: Exposes its agents as tools for other AI assistants.
*   **Professional Logging**: Structured logging for debugging and monitoring.
*   **Gemini AI Integration**: Uses Google's Gemini-1.5-flash for fast, intelligent command processing.

---

## 📁 Project Structure

```text
Narad-WhatsApp-Agent/
├── src/
│   ├── backend/
│   │   ├── agents/          # Individual AI agents (WhatsApp, GitHub, Email)
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

### 2. Twilio WhatsApp API (Recommended)
-   **Step 1**: Register at [Twilio.com](https://www.twilio.com/).
-   **Step 2**: Go to the **Twilio Console** and copy your `Account SID` and `Auth Token`.
-   **Step 3**: Navigate to **Messaging > Try it Out > Send a WhatsApp Message**. 
-   **Step 4**: Join the **Sandbox** by sending the join code to the Twilio number provided.
-   **Step 5**: Update `.env` with your `Account SID`, `Auth Token`, and the assigned Sandbox number.

---

## 🚀 Getting Started

1.  **Clone the Repo**:
    ```bash
    git clone <your-repo-link>
    cd Narad-WhatsApp-Agent
    ```

2.  **Create Virtual Environment**:
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment**: Add keys to the `.env` file (see template below).

5.  **Run the CLI**:
    ```bash
    python main.py
    ```

4.  **Run as MCP Server**:
    ```bash
    mcp run mcp_bridge.py
    ```

---

## 🧪 Usage Examples (CLI)

- **WhatsApp**: `whatsapp: send "Hello from Narad!" to "+919876543210"`
- **Gemini Brain**: Just type any query, and Narad's Gemini brain will respond.

---

## 🛠️ Roadmap

- [x] Reorganize into a modular package.
- [x] Add official Twilio support.
- [x] Add MCP Server bridge.
- [x] Integrated Google Gemini API (replacing local LLMs).
- [ ] Clone & integrate the separate **GitHub** and **Email** agents.
- [ ] Add unit tests for each agent.

---

## 🧠 Tech Stack

*   **Backend**: Python
*   **NLP**: Google Gemini 1.5 Flash
*   **WhatsApp**: Twilio API / pywhatkit
*   **Protocol**: Model Context Protocol (MCP)

---

Developed with ❤️ as an "A+ Grade" Narad Agent.




