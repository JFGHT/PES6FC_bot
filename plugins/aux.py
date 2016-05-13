# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-13 00:16:58
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 03:03:35


import telebot              # API bot library
from telebot import types   # API bot types
import sys 
sys.path.append("/home/supremoh/telegramBot/workspace")
from plugins.shared import *   # Global variables
from plugins.file_processing import *



##
## @brief  Checks if commands are available for this user
##
## @param  user_id     user if of the person who wrote the message 
##
## @return  True if it's available
##

def authorization(user_id):
   return (user_id not in BLOCKS and (read_file('reg', 'data/all_people.txt').rstrip() == 'true' or user_id in ADMIN))



##
## @brief  Sends message using private conversation
##
## @param  m     message object where command is found
## @param  message     Text to send to this user  
##

def send_private_message(m, message):
    bot.send_message(m.from_user.id, message)



##
## @brief  Sends message using private conversation with no link preview
##
## @param  m     message object where command is found
## @param  message     Text to send to this user  
##

def send_private_message_nlp(m, message):
    bot.send_message(m.from_user.id, message, disable_web_page_preview=True)



##
## @brief  Checks if message comes from an authorized group      
##
## @param  m     message object
##
## @return  True if message was sent on an authorized group
##

def group_check(m):
    return ((m.chat.type == 'group' or m.chat.type == 'supergroup') and (m.chat.id in GROUPS))



##
## @brief  Record id of users who message around the bot
##
## @param  m     message object
##

def record_uid(m):
   global USERS
   if m.from_user.username.lower() not in USERS:
       USERS[m.from_user.username.lower()] = m.from_user.id
       write_file('json', 'data/users.json', USERS)


##
## @brief  Saves bot around activity in log file
##
## @param  m     message object
##

def record_log(m):
   if m.content_type == 'text':
      if m.chat.id > 0:                                            # Conversación privada
         message = str(m.chat.first_name) + " (" + str(m.chat.id) + "): " + m.text
      else:                                                        # Grupos
         message = m.from_user.username + '(' + str(m.from_user.id) + ') in "' + m.chat.title + '"[' + str(m.chat.id) + ']: ' + m.text

      print(message)
      with open('log.txt', 'a') as __log:
         __log.write(message + "\n")



##
## @brief  Records an exception in log file
##
## @param  em     exception message
##

def record_exception(em):
   with open('log.txt', 'a') as __log:
      __log.write(em + '\n')