FROM python:3.9-slim

RUN apt-get update
RUN apt-get install -y curl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod u+x kubectl && mv kubectl /bin/kubectl

WORKDIR /app

COPY main.py /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["/app/main.py"]