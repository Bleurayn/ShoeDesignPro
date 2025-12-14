# Multi-stage: Build slim, secure image
FROM python:3.12-slim AS base

# Security best practices
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

# Install deps (minimal)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apt-get update && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy code
COPY app.py .

# Runtime
USER appuser
EXPOSE 8000  # Future Flask web

ENTRYPOINT ["python", "app.py"]
