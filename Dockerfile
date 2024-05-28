
FROM python:3.9-slim

WORKDIR /multimodal-ai-chat

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

CMD ["streamlit", "run", "app.py"]