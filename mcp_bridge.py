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
async def send_whatsapp(message: str, to_number: str, use_twilio: bool = False) -> str:
    """
    Sends a WhatsApp message to a specific phone number.
    Args:
        message: The text content to send.
        to_number: The recipient's number (e.g., '+919876543210').
        use_twilio: Whether to use the official Twilio API (True) or WhatsApp Web (False).
    """
    logger.info(f"MCP Tool Request: Send message to {to_number}")
    agent = WhatsAppAgent(use_twilio=use_twilio)
    # The agent.run expects a string command, so we format it
    command = f'send "{message}" to "{to_number}"'
    return agent.run(command)

if __name__ == "__main__":
    logger.info("🚀 Starting Narad MCP Server...")
    mcp.run()
