# Importing libraries
from dotenv import load_dotenv
from os import getenv

# Loading environment variables
load_dotenv()

# Defining class
class Config:
    FLASK_PORT = int(getenv("FLASK_PORT", 5000))
    FLASK_HOST = getenv("FLASK_HOST", "0.0.0.0")
    FLASK_DEBUG = getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "t", "yes")