from time import sleep
from celery import Celery # type: ignore
from PIL import Image # type: ignore
import pytesseract # type: ignore


celery_app = Celery(
    "worker",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="redis://redis:6379/0"
)

celery_app.conf.task_routes = {"app.tasks.*": {"queue": "default"}}

@celery_app.task(name="ocr_task")
def ocr_task(image_path: str):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)