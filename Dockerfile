FROM python:3.10-slim


WORKDIR /rag_bot

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files (excluding model & db)
COPY ./app ./app
COPY requirements.txt .
COPY README.md .

# Install dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
