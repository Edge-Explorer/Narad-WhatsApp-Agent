# src/backend/database/memory.py
import sqlite3
import os
from typing import List, Dict
from src.backend.utils.logger import setup_logger

logger = setup_logger("MemoryManager")

class MemoryManager:
    """Manages local, free SQLite database for conversation context."""
    
    def __init__(self, db_path: str = "data/narad_memory.db"):
        self.db_path = db_path
        self._init_db()
        
    def _init_db(self):
        """Creates the necessary tables if they don't exist."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversation_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                speaker TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        
    def save_message(self, speaker: str, message: str):
        """Saves a message to the history."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO conversation_history (speaker, message) VALUES (?, ?)', (speaker, message))
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"❌ Failed to save message: {e}")
            
    def get_context(self, limit: int = 5) -> str:
        """Retrieves the last N messages as a context string for Gemini."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT speaker, message FROM conversation_history ORDER BY timestamp DESC LIMIT ?', (limit,))
            rows = cursor.fetchall()
            conn.close()
            
            # Format history in reverse for Gemini
            history = [f"{speaker}: {message}" for speaker, message in reversed(rows)]
            return "\n".join(history)
        except Exception as e:
            logger.error(f"❌ Failed to retrieve context: {e}")
            return ""

    def clear_memory(self):
        """Resets the history."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('DELETE FROM conversation_history')
            conn.commit()
            conn.close()
            logger.info("🗑️ Memory cleared.")
        except Exception as e:
            logger.error(f"❌ Failed to clear memory: {e}")
