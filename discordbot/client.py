"""d
"""
import logging
import discord


class BotClient(discord.Client):
    """d
    """
    async def on_ready(self):
        """d
        """
        logging.info('Logged on as %s', self.user)

    async def on_message(self, message: discord.Message):
        """d
        """
        if message.author == self.user:
            return

        if message.content == 'ping':
            logging.info('Recieved ping.')
            await message.channel.send('pong')
            logging.info('Pong sent.')
