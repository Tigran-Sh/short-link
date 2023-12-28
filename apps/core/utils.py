from apps.core.config import settings


def generate_api_prefix(prefix: str):
    return f'{settings.API_VERSION}{prefix}'
