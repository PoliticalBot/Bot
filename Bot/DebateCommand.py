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
import urllib2
import json

INFORMACION_COMMAND, DEBATE_COMMAND, REPLY_LEYES, PARTIDOS, REPLY_PARTIDOS, BUSQUEDA, REPLY_TEMA, SELECT_TEMA, ACCEPT_TEMA, REPLY_OPTIONS = range(10)

class DebateCommand (object):
    
    @staticmethod
    def setTimeDebate(bot, update, sec):
        bot.sendMessage(update.message.chat_id, text='Comienza el debate, disponéis de ' + str(sec) + ' segundos.')
        time.sleep(sec)
        bot.debate_time = None
        bot.sendMessage(update.message.chat_id, text='El tiempo del debate ha finalizado.')
        
    @staticmethod
    def reply_main_options(bot, update):
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
            bot.sendMessage(update.message.chat_id, text='Selecciona el tiempo de duración del debate (segundos):')
            return REPLY_OPTIONS
            
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
            return BUSQUEDA
        
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
        user = update.message.from_user
        user_reply = update.message.text
        message_bot = 'De acuerdo, el tema escogido para el debate será "' + user_reply.encode('utf8') +'"'
        bot.debate_theme = user_reply.encode('utf8')
        
        if (hasattr('bot', 'debate_time')):
            bot.sendMessage(update.message.chat_id, text='El debate tendrá una duración limitada de ' + bot.debate_time + ' segundos.')
            t = threading.Thread(target=setTimeDebate, name='setTimeDebate', args=(bot, update))
            t.start()
            
        bot.sendMessage(update.message.chat_id, text=message_bot)
        message_bot = 'Recuerda que podeís utilizar los comandos /informacion para obtener cualquier información que pueda enriquecer el debate, o el comando /debate para parar el debate o cambiar de tema.'
        bot.sendMessage(update.message.chat_id, text=message_bot)
        
        DebateCommand.find_debate_info(bot, update);
        
        return ConversationHandler.END
        
    @staticmethod
    def search_results(bot, update):
        bot.sendMessage(update.message.chat_id, text='Un momento, estoy buscando resultados para tu consulta...')
        bot.sendChatAction(update.message.chat_id, action='typing')
        
        word = update.message.text
        results = list()
        
        for w in word.split():
            try:
                results.extend(wn.synsets(w, lang='spa')[0].lemma_names('spa'))
            except IndexError:
                continue
        
        message_bot = ""
        
        for i in results:
            topics = Thing.getSubTopicOf(i.encode('utf8'))
            if (topics is not None):
                message_bot = message_bot + "\n" + topics
                
        if (message_bot == ""):
            bot.sendMessage(update.message.chat_id, text='No he obtenido ningún resultado por "' + update.message.text.encode('utf8') + '" :(')
            update.message.text = 'Buscar tema'
            return DebateCommand.reply_tema(bot, update)
            
        else:
            bot.sendMessage(update.message.chat_id, text='Estos son los temas obtenidos por "' + update.message.text.encode('utf8') + '" :')
            bot.sendMessage(update.message.chat_id, text=message_bot)
            bot.sendMessage(update.message.chat_id, text='Selecciona uno de los temas propuestos')
            return ACCEPT_TEMA
            
        return ConversationHandler.END
        
    @staticmethod
    def reply_options(bot, update):
        user = update.message.from_user
        user_reply = update.message.text
        bot.sendMessage(update.message.chat_id, text='El debate tendrá una duración limitada de ' + update.message.text.encode('utf8') + ' segundos.')
        bot.debate_time = int(user_reply)
        return ConversationHandler.END
        
    @staticmethod
    def find_debate_info(bot, update):
        word = bot.debate_theme
        results = list()
        programas = list()
        political_party_aux = None
        
        for w in word.split():
            try:
                results.extend(wn.synsets(w, lang='spa')[0].lemma_names('spa'))
            except IndexError:
                continue
        
        for i in results:
            programas = urllib2.urlopen("https://apirestpoliticalbot-servicerest.rhcloud.com/search/" + word)
            
        json_object = json.load(programas)
        
        if (json_object is not None):
            bot.sendMessage(update.message.chat_id, text="He encontrado la siguiente información relacionada en los programas electorales de las siguientes formaciones políticas:")
        
        index = 1
        
        for i in json_object:
            political_party = urllib2.urlopen("https://apirestpoliticalbot-servicerest.rhcloud.com/politicalParty/" + str(i["id_political_party"]))
            nameOfPoliticalParty = json.load(political_party)
            
            if (political_party_aux is None):
                political_party_aux = nameOfPoliticalParty
                string = str(index).encode('utf8') + ") " + nameOfPoliticalParty["name"].encode('utf8') + " [Sección]-> " + i["title"].encode('utf8')
                bot.sendMessage(update.message.chat_id, text=string)
                index += 1

            elif (nameOfPoliticalParty != political_party_aux):
                political_party_aux = nameOfPoliticalParty
                string = str(index).encode('utf8') + ") " + nameOfPoliticalParty["name"].encode('utf8') + " [Sección]-> " + i["title"].encode('utf8')
                bot.sendMessage(update.message.chat_id, text=string)
                index += 1
                
        #print(nameOfPoliticalParty["name"])
        
        #bot.sendMessage(update.message.chat_id, text=programas)
            
                
        
        