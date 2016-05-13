# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-13 02:22:17
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 03:06:19


import telebot              # API bot library
from telebot import types   # API bot types
from plugins.shared import *   # Global variables
from plugins.aux import *      # Auxiliar functions
from plugins.file_processing import *


##
## Command /clasificacion - ALL
## 
## @brief  Returns links to league tables
##

def command_clasificacion(m):
    message = read_file('reg', 'data/league_table.txt')
    send_private_message_nlp(m, message)



##
## Command /censo - ALL
##
## @brief  Returns a link to census
## 

def command_censo(m):
    message = read_file('reg', 'data/census.txt')
    send_private_message(m, message)



##
## Command /hilo - ALL
##
## @brief  Returns a link to thread in FC
##

def command_hilo(m):
    message = read_file('reg', 'data/thread.txt')
    send_private_message(m, message)



##
## Command /equipos - ALL
##
## @brief  Returns a list with forbidden teams
##

def command_equipos(m):
    message = read_file('reg', 'data/teams.txt').rstrip()
    send_private_message(m, message)



##
## Command /calendarioLiga - ALL
##
## @brief  Returns a list with league schedule
##

def command_calendario_liga(m):
    message = read_file('reg', 'data/league_schedule.txt').rstrip()
    send_private_message(m, message)



##
## Command /calendarioCopa - ALL
##
## @brief  Returns a list with cup schedule
##

def command_calendario_copa(m):
    message = read_file('reg', 'data/cup_schedule.txt').rstrip()
    send_private_message(m, message)



##
## Command /calendarioEurocup - ALL
##
## @brief  Returns a list with eurocup schedule
##

def command_calendario_eurocup(m):
    message = read_file('reg', 'data/eurocup_schedule.txt').rstrip()
    send_private_message(m, message)



##
## Command /info - ALL
##
## @brief  Returns info about how to begin playing with us
##

def command_info(m):
    message = read_file('reg', 'data/info.txt').rstrip()
    send_private_message(m, message)



##
## Command /admins - GROUPS
##
## @brief  Returns admin list
##

def command_admins(m):
    admins = '@caparro - @bitters - @diegoherbie53 - @raulch - @supremoh'
    send_private_message(m, '||| Admins |||\n\n' + admins)



##
## Command /ayuda - ALL
##
## @brief  Returns a help message
##

def command_ayuda(m):
    message = read_file('reg', 'data/help.txt').rstrip()
    send_private_message(m, message)
