FROM python:3.11-slim

WORKDIR /app

RUN pip install flask && \
    apt-get update && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

COPY server.py .

EXPOSE 9000

CMD ["python", "server.py"]
