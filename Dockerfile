FROM alpine

RUN apk update; apk add python3

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
