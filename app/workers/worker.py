from rq import Worker

from app.queue.redis_queue import redis_connection

# List of queues worker listens to
QUEUES = ["document-processing"]

if __name__ == "__main__":
    worker = Worker(
        QUEUES,
        connection=redis_connection
    )

    worker.work()