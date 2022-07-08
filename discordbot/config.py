"""d
"""
# pylint: disable=logging-fstring-interpolation
from os import environ
import datetime
import logging

START_TIME=datetime.datetime.today()
try:
    LEVEL=environ.get('LEVEL')
except OSError:
    LEVEL='WARNING'
    logging.info('No DebugLevel given, defaulting to WARNING')
try:
    LOG_FILE=environ.get('LOG_FILE')
except OSError:
    LOG_FILE='./data-bot/error.log'
    logging.info(f'No Log file name provided, defaulting to {LOG_FILE}')
try:
    DATABASE=environ.get()
except OSError:
    DATABASE='./data-base/database.db'
    logging.info(f'No database path provided, defaulting to {DATABASE}')
try:
    TOKEN=environ.get('DISCORD_TOKEN')
except OSError:
    TOKEN=''
    logging.critical('Discord bot token not declared as an environment variable.')
try:
    USR=environ.get('DATABASE_USR')
    PASS=environ.get('DATABASE_PASS')
    CONNECTION = f"mongodb://{USR}:{PASS}@database"
except OSError:
    CONNECTION = ''
    logging.critical('Database credentials not declared as environment variables.')
