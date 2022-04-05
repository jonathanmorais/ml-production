from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "Iris Classify"
API_PREFIX = "/api"
API_METRICS = "/metrics"

config = Config(".env")

IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)