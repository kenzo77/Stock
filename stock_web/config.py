from pathlib import Path


sqlite_path = 'sqlite:///{0}'.format(Path("D:\workspace\stock\stock\stock_web\stock.db"))
DEBUG = True
SECRET_KEY = 'secret key'
SQLALCHEMY_DATABASE_URI = sqlite_path
SQLALCHEMY_ECHO=True
SQLALCHEMY_TRACK_MODIFICATIONS = False
