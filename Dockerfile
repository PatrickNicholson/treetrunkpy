FROM python:3.10.4-alpine as pybot
RUN apk update &&\
    apk upgrade &&\
    apk add libffi-dev openssl-dev python3-dev gcc libc-dev &&\
    pip install --upgrade pip
ADD ./discordbot /home/discordbot
WORKDIR /home/discordbot
RUN pip install -r /home/discordbot/requirements.txt
VOLUME [ "/home/discordbot/data" ]
CMD ["python","./main.py","-l","DEBUG"]



FROM alpine:latest as sqlite

RUN apk add --update sqlite
RUN mkdir /db
WORKDIR /db

ENTRYPOINT ["sqlite3"]
CMD ["test.db"]