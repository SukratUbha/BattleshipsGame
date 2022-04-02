from os import environ
from dotenv import load_dotenv

# Load environment variables from file .env, stored in this directory.
load_dotenv()


class Config:
    """Set game configuration variables"""

    # Flask configuration
    BOARD_SIZE_X = environ.get('BOARD_SIZE_X')
    BOARD_SIZE_Y = environ.get('BOARD_SIZE_Y')
    NUMBER_OF_SHIPS = environ.get('NUMBER_OF_SHIPS')
    NUMBER_OF_TRIES = environ.get('NUMBER_OF_TRIES')
