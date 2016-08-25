#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
ConversationHandler)
from telegram import (ReplyKeyboardMarkup)
import telegram
import Strings
from InformationCommand import InformationCommand
from DebateCommand import DebateCommand

INFORMACION_COMMAND, DEBATE_COMMAND, REPLY_LEYES, PARTIDOS, REPLY_PARTIDOS, BUSQUEDA, REPLY_TEMA, SELECT_TEMA, ACCEPT_TEMA = range(9)

class Commands (object):
    
    logger = None
    updater = None
    
    def __init__(self, logger, updater):
        self.logger = logger
        self.updater = updater
        self.addCommands(updater.dispatcher)
    
    # Define a few command handlers. These usually take the two arguments bot and
    # update. Error handlers also receive the raised TelegramError object in error.
    
    @staticmethod
    def addCommands(dp):
         # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", Commands.start))
        dp.add_handler(CommandHandler("help", Commands.help))
        dp.add_handler(CommandHandler("about", Commands.about))
        
        # conversations
        
        conv_handler_informacion = ConversationHandler(
            entry_points=[CommandHandler('informacion', Commands.informacion)],
            
            states={
                INFORMACION_COMMAND: [RegexHandler('^(Leyes|Reformas|Partidos|Graficos|Estadisticas|Busqueda)$', InformationCommand.reply_options)],
                
                REPLY_LEYES: [MessageHandler([Filters.text], InformationCommand.reply_leyes)],
                
                #REFORMAS: [MessageHandler([Filters.photo], photo), CommandHandler('skip', skip_photo)],
                
                #PARTIDOS: [MessageHandler([Filters.location], location), CommandHandler('skip', skip_location)],
                
                #GRAFICOS: [MessageHandler([Filters.text], bio)],
                
                #ESTADISTICAS: [MessageHandler([Filters.text], None)],
                
                PARTIDOS: [RegexHandler('^(PP|PSOE|Podemos|Ciudadanos|IU|ERC|CDC|PNV)$', InformationCommand.partidos)],
                
                REPLY_PARTIDOS: [RegexHandler('^(Noticias|Programa|Candidatos)$', InformationCommand.reply_partidos)],
                
                BUSQUEDA: [MessageHandler([Filters.text], InformationCommand.search_results)]
            },
            
            fallbacks=[CommandHandler('cancel', None)]
            
            )

        dp.add_handler(conv_handler_informacion)
        
        conv_handler_debate = ConversationHandler(
            entry_points=[CommandHandler('debate', Commands.debate)],
            
            states={
                
                DEBATE_COMMAND: [RegexHandler('^(Iniciar debate|Detener debate|Opciones)$', DebateCommand.reply_options)],
                
                REPLY_TEMA: [RegexHandler('^(Seleccionar tema|Buscar tema|Sugerir tema)$', DebateCommand.reply_tema)],
                
                SELECT_TEMA: [MessageHandler([Filters.text], DebateCommand.select_tema)],
                
                ACCEPT_TEMA: [MessageHandler([Filters.text], DebateCommand.accept_tema)],
                
                #REFORMAS: [MessageHandler([Filters.photo], photo), CommandHandler('skip', skip_photo)],
                
                #PARTIDOS: [MessageHandler([Filters.location], location), CommandHandler('skip', skip_location)],
                
                #GRAFICOS: [MessageHandler([Filters.text], bio)],
                
                #ESTADISTICAS: [MessageHandler([Filters.text], None)],
                
                BUSQUEDA: [MessageHandler([Filters.text], None)]
                
            },
            
            fallbacks=[CommandHandler('cancel', None)]
            
            )

        dp.add_handler(conv_handler_debate)
    
        # on noncommand i.e message - echo the message on Telegram
        #dp.add_handler(MessageHandler([Filters.text], Commands.echo))
    
        # log all errors
        dp.add_error_handler(Commands.error)

    @staticmethod
    def start(bot, update):
        bot.sendMessage(update.message.chat_id, text=Strings.START_COMMAND)

    @staticmethod
    def help(bot, update):
        bot.sendMessage(update.message.chat_id, text=Strings.HELP_COMMAND)
        
    @staticmethod
    def informacion(bot, update):
        custom_keyboard = [['Leyes', 'Reformas', 'Partidos'], ['Graficos', 'Estadisticas', 'Busqueda'], ['Cancelar']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(update.message.chat_id, text=Strings.INFORMACION_COMMAND, reply_markup=ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True))
        
        return INFORMACION_COMMAND

    @staticmethod
    def debate(bot, update):
        custom_keyboard = [['Iniciar debate', 'Detener debate', 'Opciones']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(update.message.chat_id, text=Strings.DEBATE_COMMAND, reply_markup=ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True))
        
        return DEBATE_COMMAND
        
    @staticmethod
    def about(bot, update):
        bot.sendMessage(update.message.chat_id, text='Help!')
    
    @staticmethod
    def echo(bot, update):
        bot.sendMessage(update.message.chat_id, text=update.message.text)
        
    @staticmethod
    def error(bot, update, error):
        logger.warn('Update "%s" caused error "%s"' % (update, error))
