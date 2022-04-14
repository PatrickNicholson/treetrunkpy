"""d
"""
from os import environ
import datetime

START_TIME=datetime.datetime.today()
TOKEN=environ.get('DISCORD_TOKEN')
LOG_FILE='error.log'
LEVEL='DEBUG'
