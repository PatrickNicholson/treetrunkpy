FROM python:3.10.4-alpine

RUN apk update
RUN apk upgrade
RUN pip install discord

ADD ./discordbot /home/discordbot

WORKDIR /home/discordbot

VOLUME [ "/home/discordbot/data" ]

CMD ["python","./main.py"]