""" File: main.py
This script starts and handles the Discord Bot.
"""
import argparse
import logging
import discord
from client import BotClient
from config import TOKEN, LOG_FILE

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--log', dest='loglevel',
                        choices=['INFO','DEBUG','WARNING','ERROR','CRITICAL'], default='WARNING')
    parser.add_argument('-t', '--token', dest='token', type=str, default=TOKEN)
    args = parser.parse_args()

    logging.basicConfig(filename=LOG_FILE, filemode='w', encoding='utf-8',
                        format='%(asctime)s %(levelname)-8s %(message)s', level=args.loglevel)

    intents = discord.Intents.default()
    client = BotClient(intents=intents)
    logging.info('Starting Client.')
    client.run(args.token)
