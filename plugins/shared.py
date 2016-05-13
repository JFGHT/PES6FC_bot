# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-12 13:52:18
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 02:56:45


import telebot              # API bot library
from telebot import types   # API bot types
from plugins.file_processing import *


############### Global variables ################
TOKEN = read_file('reg', 'data/token.txt').rstrip()
ADMIN = read_file('json', 'data/admin.json')
GROUPS = read_file('json', 'data/groups.json')
POLES = read_file('json', 'data/poles.json')
DATES = read_file('json', 'data/dates.json')
BLOCKS = read_file('json', 'data/block.json')
USERS = read_file('json', 'data/users.json')


############## Creates bot object ###############
bot = telebot.TeleBot(TOKEN)