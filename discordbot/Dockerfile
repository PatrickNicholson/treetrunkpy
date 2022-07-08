FROM python:3.10.4-slim as pybot
RUN apt update &&\
    apt upgrade &&\
    apt install libffi-dev openssl-dev python3-dev gcc libc-dev &&\
    pip install --upgrade pip
ADD ./discordbot /home/discordbot
WORKDIR /home/discordbot
RUN pip install -r /home/discordbot/requirements.txt
VOLUME [ "/home/discordbot/data" ]
CMD ["python","./main.py","-l","DEBUG"]