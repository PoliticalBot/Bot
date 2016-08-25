#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
ConversationHandler, Job)
from Ontology.Thing import Thing
from telegram import (ReplyKeyboardMarkup)
import telegram
import Strings
import threading
import thread
import time
from nltk.corpus import wordnet as wn

INFORMACION_COMMAND, DEBATE_COMMAND, REPLY_LEYES, PARTIDOS, REPLY_PARTIDOS, BUSQUEDA, REPLY_TEMA, SELECT_TEMA, ACCEPT_TEMA = range(9)

class DebateCommand (object):
    
    @staticmethod
    def setTimeDebate(bot, update, sec):
        bot.sendMessage(update.message.chat_id, text='Comienza el debate, disponéis de ' + str(sec) + ' segundos.')
        time.sleep(sec)
        bot.sendMessage(update.message.chat_id, text='El tiempo del debate ha finalizado.')
        
    @staticmethod
    def reply_options(bot, update):
        user = update.message.from_user
        user_reply = update.message.text
        
        if (user_reply == 'Iniciar debate'):
            custom_keyboard = [['Seleccionar tema', 'Buscar tema', 'Sugerir tema']]
            reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
            bot.sendMessage(update.message.chat_id, text='Antes de iniciar el debate, deberás escoger un tema:', reply_markup=ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True))
            return REPLY_TEMA
            
        elif (user_reply == 'Detener debate'):
            bot.sendMessage(update.message.chat_id, text='Y hasta aquí el debate, espero que hayáis podido establecer una buena comunicación. Hasta la próxima \xf0\x9f\x98\x89')
            
        elif (user_reply == 'Opciones'):
            bot.sendMessage(update.message.chat_id, text='Aquí podéis modificar las diferentes opciones del debate')
            thread.start_new_thread(DebateCommand.setTimeDebate, (bot, update, 50))
            #t = threading.Thread(target=setTimeDebate, name='setTimeDebate', args=(bot, update))
            #t.start()
            
        else:
            bot.sendMessage(update.message.chat_id, text='Disculpa, no te he entendido :(')
            return Commands.informacion(bot, update)
            
        return ConversationHandler.END
        
    @staticmethod
    def reply_tema(bot, update):
        user = update.message.from_user
        user_reply = update.message.text
        
        if (user_reply == 'Seleccionar tema'):
            bot.sendMessage(update.message.chat_id, text='Selecciona uno de los siguientes temas:')
            bot.sendMessage(update.message.chat_id, text=Strings.TEMAS_PRINCIPALES)
            return SELECT_TEMA
            
        elif (user_reply == 'Buscar tema'):
            bot.sendMessage(update.message.chat_id, text='Introduce el un término de búsqueda:')
        
        elif (user_reply == 'Sugerir tema'):
            bot.sendMessage(update.message.chat_id, text='Está bien, podríamos hablar de...')
            
        else:
            bot.sendMessage(update.message.chat_id, text='Disculpa, no te he entendido :(')
            return Commands.informacion(bot, update)
            
    @staticmethod
    def select_tema(bot, update):
        user = update.message.from_user
        user_reply = update.message.text
        message_bot = 'Está bien, debatiremos sobre ' + user_reply.encode('utf8')
        bot.sendMessage(update.message.chat_id, text='Dentro de ' + user_reply.encode('utf8') + ' podemos diferenciar los siguientes temas:')
        bot.sendMessage(update.message.chat_id, text=Thing.getSubTopicOf(user_reply.encode('utf8')))
        bot.sendMessage(update.message.chat_id, text="Selecciona uno")
        return ACCEPT_TEMA
        
    @staticmethod
    def accept_tema(bot, update):
        print("caca")
        user = update.message.from_user
        user_reply = update.message.text
        message_bot = 'De acuerdo, el tema escogido para el debate será "' + user_reply.encode('utf8') +'"'
        bot.sendMessage(update.message.chat_id, text=message_bot)
        message_bot = 'Recuerda que podeís utilizar los comandos /informacion para obtener cualquier información que pueda enriquecer el debate, o el comando /debate para parar el debate o cambiar de tema.'
        bot.sendMessage(update.message.chat_id, text=message_bot)
        return ConversationHandler.END