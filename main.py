#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from Bot.Commands import Commands

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():

    # Create the EventHandler and pass it your bot's token.
    updater = Updater("200170954:AAHiULX1eL3kn1WcSTKlEJ4kzMKoq7zjSic")
    
    # Add commands to the dispatcher
    Commands(logger, updater)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()