from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Application settings
APP_NAME = "ULPF"
APP_VERSION = "1.0.0"
DEBUG = True

# Log settings
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "ulpf.log"

# Database settings
DATABASE_URL = "sqlite:///./ulpf.db"