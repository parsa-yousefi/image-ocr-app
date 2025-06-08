from celery import Celery # type: ignore


app = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/0"
)
app.autodiscover_tasks(["app.tasks.*"])
