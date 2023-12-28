import os

from pydantic_settings import BaseSettings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Settings(BaseSettings):
    API_VERSION: str = '/api/v1/'
    APP_NAME: str = os.environ.get('APP_NAME')
    APP_URL: str = os.environ.get('APP_URL')

    # DB
    DB_HOST: str = os.getenv('POSTGRES_HOST')
    DB_USER: str = os.getenv('POSTGRES_USER')
    DB_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    DB_NAME: str = os.getenv('POSTGRES_DB')

    @property
    def DATABASE_URL(self):
        return f'postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}'


# global instance
settings = Settings()
