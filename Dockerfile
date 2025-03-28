FROM python:3.11

RUN pip install yt-dlp flask flask-cors

WORKDIR /app

COPY . .

EXPOSE 10000

CMD ["python", "-u", "server.py"]
