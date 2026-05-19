from redis import Redis
from rq import Queue

from app.core.config.settings import settings

redis_connection = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

queue = Queue(
    "document-processing",
    connection=redis_connection
)