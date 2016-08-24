#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
ConversationHandler)
from telegram import (ReplyKeyboardMarkup)
import Websites
import Commands
import telegram
import Strings
from nltk.corpus import wordnet as wn

INFORMACION_COMMAND, DEBATE_COMMAND, REPLY_LEYES, BUSQUEDA, REPLY_TEMA, SELECT_TEMA, ACCEPT_TEMA = range(7)

class InformationCommand (object):
    
    index_laws = 0;
    
    @staticmethod
    def reply_options(bot, update):
        user = update.message.from_user
        user_reply = update.message.text
        
        if (user_reply == 'Leyes'):
            url = Websites.LAWS_SITES[InformationCommand.index_laws]
            custom_keyboard = [['Mas_informacion', 'Cancelar']]
            reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
            bot.sendMessage(update.message.chat_id, text=url, reply_markup=ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True))
            return REPLY_LEYES
            
        elif (user_reply == 'Reformas'):
            InformationCommand.reformas(bot, update)
            
        elif (user_reply == 'Partidos'):
            InformationCommand.partidos(bot, update)
            
        elif (user_reply == 'Graficos'):
            InformationCommand.graficos(bot, update)
            
        elif (user_reply == 'Estadisticas'):
            InformationCommand.estadisticas(bot, update)
            
        elif (user_reply == 'Busqueda'):
            InformationCommand.busqueda(bot, update)
            bot.sendMessage(update.message.chat_id, text='Introduce un criterio de búsqueda:')
            return BUSQUEDA
            
        elif (user_reply == 'Cancelar'):
            pass
            
        else:
            bot.sendMessage(update.message.chat_id, text='Disculpa, no te he entendido :(')
            return Commands.informacion(bot, update)
            
        return ConversationHandler.END
        
    @staticmethod
    def search_results(bot, update):
        results = wn.synsets(update.message.text)[0].lemma_names('spa')
        bot.sendMessage(update.message.chat_id, text='Estos son los resultados obtenidos por "' + update.message.text + '" :')
        bot.sendMessage(update.message.chat_id, text=results)
        return ConversationHandler.END
        
    @staticmethod
    def leyes(bot, update):
        if (InformationCommand.index_laws >= len(Websites.LAWS_SITES)):
            bot.sendMessage(update.message.chat_id, text='Por ahora no tengo más información que ofrecerte :(')
            return ConversationHandler.END
        
        url = Websites.LAWS_SITES[InformationCommand.index_laws]
        
        custom_keyboard = [['Mas_informacion', 'Cancelar']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(update.message.chat_id, text=url, reply_markup=ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True))
        return REPLY_LEYES
        
    @staticmethod
    def reply_leyes(bot, update):
        user = update.message.from_user
        user_reply = update.message.text
        
        if (user_reply == 'Mas_informacion'):
            InformationCommand.index_laws += 1
            return InformationCommand.leyes(bot, update)
            
        elif (user_reply == 'Cancelar'):
            return ConversationHandler.END
            
        else:
            bot.sendMessage(update.message.chat_id, text='Disculpa, no te he entendido :(')
            return leyes(bot, update)
        
    @staticmethod
    def reformas(bot, update):
        pass
        
    @staticmethod
    def partidos(bot, update):
        pass
    
    @staticmethod
    def graficos(bot, update):
        pass
        
    @staticmethod
    def estadisticas(bot, update):
        pass
        
    @staticmethod
    def busqueda(bot, update):
        pass