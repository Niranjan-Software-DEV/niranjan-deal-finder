import sys
from pathlib import Path

# Add the backend directory to sys.path so the FastAPI app can find its modules
backend_path = Path(__file__).parent.parent / "backend"
sys.path.append(str(backend_path))

# Import the FastAPI application
from backend.main import app

# This allows Vercel to pick up the app instance
