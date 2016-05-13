# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-11 18:41:22
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 02:56:04

 
import telebot              # API bot library
from telebot import types   # API bot types
import sys
import pkgutil
import importlib
import sys
from plugins.admin import *
from plugins.aux import *
from plugins.shared import *
from plugins.pole import *
from plugins.pes import *
from plugins.fun import *
from plugins.file_processing import *

reload(sys)                           # python 2
sys.setdefaultencoding("utf-8")       #


#################################################
## Listener

##
## @brief  Receives all messages that bot listens and records important info
##
## @param  messages     list of messages
##

def listener(messages):
    for m in messages:
        record_uid(m)   # Record user id
        record_log(m)   # Log file



## Declare last function as bot's listener
bot.set_update_listener(listener)


#################################################
## Functions - Message handlers

##
## @brief  Send a welcome message if anyone joins the group
## 
## @param  m     message object
##

@bot.message_handler(content_types=['new_chat_participant'])
def welcome(m):
    message = 'Bienvenido @' + m.new_chat_participant.username + '!! ' + read_file('reg', 'data/welcome.txt')
    bot.send_message(m.chat.id, message.rstrip(), disable_web_page_preview=True)



##
## @brief  Send a farewall message if anyone leaves the group
## 
## @param  m     message object
##

@bot.message_handler(content_types=['left_chat_participant'])
def farewall(m):
    bot.send_message(m.chat.id, 'Dep, siempre saludaba')



##
## @brief  Recognize commands on messages and call the right function
##
## @param  m     message object
##

@bot.message_handler(func=lambda msg:msg.text.encode("utf-8"))     # python 2
# @bot.message_handler(content_types=['text'])                     # python 3
def commands(m):
    if authorization(m.from_user.id):
        c = [
            '/equipos', '/pole', '/insultar', 
            '/clasificacion', '/censo', '/hilo', 
            '/getcommands', '/setcommands', '/info', 
            '/ayuda', '/nohomo', '/stats',
            '/admins', '/calendarioliga', '/calendariocopa',
            '/calendarioeurocup', '/echo', '/block', 
            '/unblock'
            ]
            
        if c[0] in m.text[:len(c[0])].lower():      # equipos
            command_equipos(m)
        elif c[1] in m.text[:len(c[1])].lower():    # pole
            command_pole(m)
        elif c[2] in m.text[:len(c[2])].lower():    # insultar
            command_insultar(m)
        elif c[3] in m.text[:len(c[3])].lower():    # clasificacion
            command_clasificacion(m)
        elif c[4] in m.text[:len(c[4])].lower():    # censo
            command_censo(m)
        elif c[5] in m.text[:len(c[5])].lower():    # hilo
            command_hilo(m)

        # ADMIN
        elif c[6] in m.text[:len(c[6])].lower():    # getcommands
            command_get_commands(m)
        elif c[7] in m.text[:len(c[7])].lower():    # setcommands
            command_set_commands(m)

        elif c[8] in m.text[:len(c[8])].lower():    # info
            command_info(m)
        elif c[9] in m.text[:len(c[9])].lower():    # ayuda
            command_ayuda(m)
        elif c[10] in m.text[:len(c[10])].lower():  # nohomo
            command_nohomo(m)
        elif c[11] in m.text[:len(c[11])].lower():  # stats
            command_stats(m)
        elif c[12] in m.text[:len(c[12])].lower():  # admin
            command_admins(m)
        elif c[13] in m.text[:len(c[13])].lower():  # calendarioLiga
            command_calendario_liga(m)
        elif c[14] in m.text[:len(c[14])].lower():  # calendarioCopa
            command_calendario_copa(m)
        elif c[15] in m.text[:len(c[15])].lower():  # calendarioEurocup
            command_calendario_eurocup(m)

        # ADMIN
        elif c[16] in m.text[:len(c[16])].lower():  # echo
            command_echo(m)
        elif c[17] in m.text[:len(c[17])].lower():  # block
            command_block(m)
        elif c[18] in m.text[:len(c[18])].lower():  # unblock
            command_unblock(m)

        elif 'pole' in m.text.lower():
            command_pole_check(m)



#############################################
## Requests

## Continue working even if there are errors
bot.polling(none_stop=True)