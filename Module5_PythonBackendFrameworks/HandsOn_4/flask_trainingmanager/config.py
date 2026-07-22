import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key_123')
    # Uses a local SQLite file for fast desktop development
    SQLALCHEMY_DATABASE_URI = 'sqlite:///corporate_training.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True