class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = 'postgres'
    DB_PASSWORD = 'etereg14'
    DB_NAME = 'flask_tms'
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
