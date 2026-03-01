# src/backend/agents/base_agent.py
from abc import ABC, abstractmethod
from src.backend.utils.logger import setup_logger

class BaseAgent(ABC):
    """Base class for all agents in the Narad system."""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = setup_logger(name)
        self.logger.info(f"🚀 Initializing {self.name}...")

    @abstractmethod
    def run(self, command: str) -> str:
        """Processes the given command and returns a response."""
        pass

