"""
Narad MCP Server Bridge
Exposes WhatsApp and other agents as MCP Tools.
"""
from typing import Any
import os
import asyncio
from mcp.server.fastmcp import FastMCP
from src.backend.agents.whatsapp_agent import WhatsAppAgent
from src.backend.utils.logger import setup_logger

logger = setup_logger("MCP-Server")

# Create the MCP Server
mcp = FastMCP("Narad")

@mcp.tool()
async def search_web(query: str, max_results: int = 3) -> str:
    """Performs a 100% free web search using DuckDuckGo."""
    from src.backend.core.tools import NaradTools
    return NaradTools.web_search(query, max_results)

@mcp.tool()
async def read_doc(file_path: str) -> str:
    """Reads content from a PDF or DOCX file inside the data/ folder."""
    from src.backend.core.tools import NaradTools
    return NaradTools.read_document(file_path)

@mcp.tool()
async def get_stats() -> str:
    """Gets local system CPU and RAM usage stats."""
    from src.backend.core.tools import NaradTools
    return NaradTools.get_system_stats()

@mcp.tool()
async def send_whatsapp(message: str, to_number: str, use_twilio: bool = True) -> str:
    """Sends a WhatsApp message via Twilio."""
    from src.backend.agents.whatsapp_agent import WhatsAppAgent
    agent = WhatsAppAgent(use_twilio=use_twilio)
    command = f'send "{message}" to "{to_number}"'
    return agent.run(command)

if __name__ == "__main__":
    logger.info("🚀 Starting Narad " + "Extreme " + "MCP Server...")
    mcp.run()

