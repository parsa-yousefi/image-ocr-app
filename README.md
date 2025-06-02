# 🖼️ image_ocr_app

A Dockerized asynchronous OCR (Optical Character Recognition) microservice built with FastAPI, Celery, RabbitMQ, Redis, and Nginx.

This project allows users to upload images, process them asynchronously using OCR, and retrieve the extracted text using task IDs.

---

## 🚀 Tech Stack

- **FastAPI** – Web framework for handling image uploads and API endpoints.
- **Celery** – Task queue for managing asynchronous background jobs.
- **RabbitMQ** – Message broker for handling task queue communication.
- **Redis** – Backend for Celery task results and state tracking.
- **Tesseract OCR** – OCR engine for extracting text from images.
- **Nginx** – Reverse proxy server to expose FastAPI app externally.
- **Docker Compose** – For managing multi-container setup.

---

## 📦 Features

- Upload images via REST API
- Process images asynchronously in background
- Retrieve OCR results using task ID
- Clean service separation using Docker
- Simple and extensible architecture

---

## ⚙️ Prerequisites

- Docker
- Docker Compose
- Git

---

## 🧰 Installation & Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/image_ocr_app.git
   cd image_ocr_app
   ```

2. **Build and start the services**:

   ```bash
   docker-compose up --build
   ```

3. **Access the API**:

   - FastAPI docs: [http://localhost/docs](http://localhost/docs)
   - Nginx exposed API: [http://localhost](http://localhost)

---

## 🧪 Example Workflow

1. **Upload an image**:

   ```bash
   curl -X POST "http://localhost/upload" -F "file=@example.png"
   ```

   Response:

   ```json
   {
     "task_id": "9d0f4a37-4e19-4c76-93df-b9a1a0e8d2aa"
   }
   ```

2. **Check task result**:

   ```bash
   curl http://localhost/result/9d0f4a37-4e19-4c76-93df-b9a1a0e8d2aa
   ```

---

## 🗂️ Project Structure

```
image_ocr_app/
│
├── app/
│   ├── main.py            # FastAPI app with upload and result endpoints
│   ├── celery_worker.py   # Celery application and task loader
│   ├── tasks.py           # OCR task logic
│   └── utils.py           # (optional) Helpers for file handling or OCR
│
├── Dockerfile             # For building FastAPI + Celery image
├── docker-compose.yml     # Multi-container setup
├── nginx/
│   └── nginx.conf         # Nginx reverse proxy configuration
└── README.md              # Project documentation
```

---

## 🧹 TODO

- Add authentication
- Add image validation
- Support multiple OCR languages
- Store extracted text in a database

---

## 🧠 Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [Celery](https://docs.celeryq.dev/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---
