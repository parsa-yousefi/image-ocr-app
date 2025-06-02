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
