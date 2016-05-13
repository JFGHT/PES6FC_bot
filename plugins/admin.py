# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-11 18:39:10
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 03:05:54


import telebot              # API bot library
from telebot import types   # API bot types
from plugins.shared import *   # Global variables
from plugins.aux import *      # Auxiliar functions
from plugins.file_processing import *


##
## Command /getcommands - ADMIN
## 
## @brief  Returns true if commands are available for all people
##

def command_get_commands(m):
    global ADMIN
    if m.from_user.id in ADMIN:
        bot.send_message(m.chat.id, read_file('reg', 'data/all_people.txt').strip())



##
## Command /setcommands - ADMIN
## 
## @brief  Sets commands for all people or just for ADMINS
##

def command_set_commands(m):
    global ADMIN
    if m.from_user.id in ADMIN:
        flag = m.text[13:].strip()
        if flag == '':
            flag = 'false'
        
        write_file('reg', 'data/all_people.txt', flag)
        bot.send_message(m.chat.id, 'Enabled commands? ' + flag)



##
## Command /block - ADMIN
##
## @brief  Blocks an user from using the bot
##

def command_block(m):
    global ADMIN, USERS, BLOCKS
    if m.from_user.id in ADMIN:
        username = m.text[8:].lower()
        if username in USERS:
            uid = USERS[username]
            if uid in BLOCKS:
                bot.reply_to(m, '@' + username + ' ya se encuentra bloqueado')
            else:
                BLOCKS.append(uid)
                write_file('json', 'data/block.json', BLOCKS)
                bot.reply_to(m, '@' + username + ' acaba de ser bloqueado')
        else:
            bot.reply_to(m, 'No conozco a @' + username)



##
## Command /unblock - ADMIN
##
## @brief  Unblocks an user from using the bot
##

def command_unblock(m):
    global ADMIN, USERS, BLOCKS
    if m.from_user.id in ADMIN:
        username = m.text[10:].lower()
        if username in USERS:
            uid = USERS[username]
            if uid in BLOCKS:
                BLOCKS.remove(uid)
                write_file('json', 'data/block.json', BLOCKS)
                bot.reply_to(m, '@' + username + ' ha sido desbloqueado')
            else:
                bot.reply_to(m, '@' + username + ' no se encuentra bloqueado')
        else:
            bot.reply_to(m, 'No conozco a @' + username)



##
## Command /getblocks - ADMIN
##
## @brief  Returns a list with blocked people
##

# def command_getblocks(m):
#     global ADMIN, USERS, BLOCKS
#     if m.from_user.id in ADMIN:
#         for blocked in BLOCKS:
#             for username, uid in USERS:
#                 if 



##
## Command /echo - ADMIN
##
## @brief  Sends the message it receives for the specified group
##

def command_echo(m):
    global ADMIN
    if m.from_user.id in ADMIN:
        message = m.text[5:]
        bot.send_message(GROUPS[0], message)