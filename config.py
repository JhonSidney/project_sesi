import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///colegio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123'
