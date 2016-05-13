# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-13 00:21:56
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 03:06:56


import telebot              # API bot library
from telebot import types   # API bot types
import datetime
from plugins.shared import *   # Global variables
from plugins.aux import *      # Auxiliar functions
from plugins.file_processing import *


##
## @brief  Converts unix message time to readable format
##
## @param  unix_time     Unix message time
##
## @return  Readable Spanish date
##

def get_readable_date(unix_time):
    return datetime.datetime.fromtimestamp(unix_time).strftime('%d-%m-%Y')



##
## @brief  Checks if message is pole or not
##
## @param  m     message object
##

def command_pole_check(m):
    global POLES, DATES
    if group_check(m):
        date = get_readable_date(m.date)
        if date not in DATES:
            bot.reply_to(m, 'Menudo hijo de puta, tienes unas poles del copón. De fails nada, tu das gloria. ' +
                            'Menudas poles tienes, hijo de la gran puta. Olvídate de dejarlo, potencia esa mente tan espectacular ' + 
                            'que tienes, hijo de una perra sarnosa. Qué puta envidia me das!')
    
            pole_man = m.from_user.username
            DATES[date] = pole_man
            
            if pole_man in POLES:
                POLES[pole_man] += 1
            else:
                POLES[pole_man] = 1
            
            write_file('json', 'data/poles.json', POLES)
            write_file('json', 'data/dates.json', DATES)



##
## Command /pole - GROUPS
##
## @brief  Returns the user who made the last pole
##

def command_pole(m):
    global POLES, DATES
    if group_check(m): 
        date = get_readable_date(m.date)
        if date in DATES:
            bot.send_message(m.chat.id, '||| Poleador del día |||\n\n@' + DATES[date])
        else: 
            bot.send_message(m.chat.id, 'A qué esperas, hijo de puta? Haz la puñetera pole de una vez.')



##
## Command /stats - GROUPS
##
## @brief  Returns a list with all pole men
##

def command_stats(m):
    global POLES
    if group_check(m): 
        message = '||| Listado de poleadores |||\n\n'
        for key,value in POLES.items():
            message += '@' + key + ' = ' + str(value) + '\n'
        bot.send_message(m.chat.id, message)