FROM python:3.11-alpine

WORKDIR /app

RUN pip install flask && \
    apk add --no-cache git && \
    git config --global --add safe.directory /repo

COPY server.py .

EXPOSE 9000

CMD ["python", "server.py"]
