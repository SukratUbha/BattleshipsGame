from os import environ
from dotenv import load_dotenv

# Load environment variables from file .env, stored in this directory.
load_dotenv()


class Config:
    """Set game congiguration variables"""

    # Flask configuration
    BOARD_SIZE = environ.get('BOARD_SIZE')
    NUMBER_OF_SHIPS = environ.get('NUMBER_OF_SHIPS')
