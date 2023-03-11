#!/usr/bin/python3
"""
initialize the models package
"""

from dotenv import load_dotenv
from os import getenv


load_dotenv()  # Loads environment variables from .env file


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
