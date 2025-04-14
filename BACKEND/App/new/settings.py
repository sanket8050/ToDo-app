from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")

except FileNotFoundError:
    config = Config(".env.example")

Database_url = config("Database_url", cast=Secret)