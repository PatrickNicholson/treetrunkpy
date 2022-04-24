"""d
"""
from os import environ
import datetime
import logging

START_TIME=datetime.datetime.today()
try:
    TOKEN=environ.get('DISCORD_TOKEN')
except OSError:
    TOKEN=''
    logging.info('Discord bot token not declared as an environment variable.')
LOG_FILE='./data/error.log'
LEVEL='DEBUG'
