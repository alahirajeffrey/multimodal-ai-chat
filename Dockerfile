
FROM python:3.9-slim

WORKDIR /multimodal-ai-chat

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set the environment variable to avoid creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Set the environment variable to buffer stdout and stderr
ENV PYTHONUNBUFFERED 1

CMD ["streamlit", "run", "app.py"]