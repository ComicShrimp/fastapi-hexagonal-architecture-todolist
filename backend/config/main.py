import logging

from .container import Container
from .settings import Settings

logging.basicConfig(level=logging.INFO)

settings = Settings()

# Dependency Injection
container = Container()

container.config.from_pydantic(settings)
