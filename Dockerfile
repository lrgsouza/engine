FROM python:3.9-slim

WORKDIR /app

COPY /app /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["/app/main.py"]