FROM python:3.11

RUN pip install yt-dlp flask flask-cors

WORKDIR /app

COPY . .

CMD ["python", "-u", "server.py"]
