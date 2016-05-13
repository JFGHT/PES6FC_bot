# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-13 12:32:18
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-26 13:16:55


import telebot              # API bot library
from telebot import types   # API bot types
import random
from plugins.shared import *   # Global variables
from plugins.aux import *      # Auxiliar functions
from plugins.file_processing import *


##
## Command /insultar - GROUPS
##
## @brief  Insults someone
##

def command_insultar(m): 
    if group_check(m): 
        sentences = {
            0:"Carajaula",
            1:"Bocachancla",
            2:"Eres más inútil que un gitano sin primos",
            3:"Peinabombillas",
            4:"Gilipollas",
            5:"Mira macho vete a la mierda, de verdad",
            6:"Tienes más cuernos que un saco de caracoles",
            7:"Muerdealmohadas",
            8:"Caracartón",
            9:"Abrazafarolas",
            10:"Planchabragas",
            11:"Lamecharcos",
            12:"¿Eres tonto o pellizcas cristales?",
            13:"Cabestro",
            14:"Eres más tonto que cagar de pie",
            15:"Eres más inútil que el cenicero de una moto",
            16:"Eres tan tonto que vendiste el coche para comprar gasolina",
            17:"Eres más tonto que mear haciendo el pino",
            18:"Eres más inútil que @MrMindungui",
            19:"Tienes menos luces que la bici de un gitano"
        }
        
        insulted = m.text[10:]
    
        if insulted == '':                                  # no hay persona a la que insultar
            message = 'Pero dime a quién insulto, pedazo de inútil'
            bot.reply_to(m, message)                        # respondemos citando al mensaje
        else:
            if insulted == 'supremoh' or insulted == '@supremoh':         
                message = 'Con @supremoh no, joputa, que te reviento'
                bot.reply_to(m, message)
            elif insulted == 'PES6FC_bot':
                message = 'Tan retrasado eres que no sabes usar el puto comando?'
                bot.reply_to(m, message)
            elif insulted == '@PES6FC_bot':
                message = 'La próxima vez vas a insultar a tu prima la coja, joputa'
                bot.reply_to(m, message)
            else:
                if insulted[0] != '@':                                     
                    message = sentences[random.randrange(len(sentences))] + ' @' + insulted
                else:                                                                   
                    message = sentences[random.randrange(len(sentences))] + ' ' + insulted
                bot.send_message(m.chat.id, message)     



##
## Command /nohomo - GROUPS
##
## @brief  Returns a nohomo picture
##

def command_nohomo(m):
    if group_check(m): 
        sihomo = read_file('reg', 'data/nohomo.txt').split()
        message = sihomo[random.randrange(len(sihomo))]
        bot.send_message(m.chat.id, message)