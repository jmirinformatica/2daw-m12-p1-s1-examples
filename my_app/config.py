from os import environ, path
from dotenv import load_dotenv

file_dir = path.abspath(path.dirname(__file__))
root_dir = path.dirname(file_dir)
load_dotenv(path.join(root_dir, '.env'))

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + path.join(root_dir, environ.get('SQLITE_FILE_RELATIVE_PATH'))