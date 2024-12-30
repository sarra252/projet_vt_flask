import os

class Config:
    SECRET_KEY = os.urandom(32)  # Génère une clé secrète de manière sécurisée
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Utilise SQLite pour la base de données
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactive les notifications de modification de SQLAlchemy
