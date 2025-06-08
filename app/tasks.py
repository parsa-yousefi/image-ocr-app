from time import sleep
from .celery_worker import app # type: ignore
from PIL import Image # type: ignore
import pytesseract # type: ignore



@app.task(name="ocr_task")
def ocr_task(image_path: str):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return str(e)