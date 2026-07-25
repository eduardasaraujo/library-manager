class Config:
    SECRET_KEY = "library-manager-secret"

    SQLALCHEMY_DATABASE_URI = "sqlite:///library.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False