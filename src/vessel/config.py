import os

from dotenv import load_dotenv

load_dotenv()

# Get database connection credentials from environment variables
DATABASE_SERVER_URL = os.getenv("SILVER_LAKEHOUSE_DATABASE_SERVER_URL")
DATABASE = os.getenv("SILVER_LAKEHOUSE_DATABASE")
AUTH_METHOD = os.getenv("SILVER_LAKEHOUSE_AUTH_METHOD")
