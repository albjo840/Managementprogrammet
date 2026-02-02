FROM python:3.11-alpine

WORKDIR /app

RUN pip install flask && \
    apk add --no-cache git

COPY server.py .

EXPOSE 9000

CMD ["python", "server.py"]
