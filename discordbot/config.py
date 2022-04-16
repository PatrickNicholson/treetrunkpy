"""d
"""
from os import environ
import datetime

START_TIME=datetime.datetime.today()
TOKEN=environ.get('DISCORD_TOKEN')
LOG_FILE='./data/error.log'
LEVEL='DEBUG'
