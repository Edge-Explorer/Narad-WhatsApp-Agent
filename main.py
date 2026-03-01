import sys
import os

# Ensure the src directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from src.backend.core.narad_core import start_narad

if __name__ == "__main__":
    start_narad()
