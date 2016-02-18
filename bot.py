# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import sys
import datetime

reload(sys) 
sys.setdefaultencoding("utf-8")

 
TOKEN = '196817759:AAGPd3ZCCnByvXjUE-MHZRD6ZIGtR9uWr0M' # Nuestro tokken del bot (el que @BotFather nos dió).
HORA_POLE = '23:25'
ADMIN = [6216877]

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text': # Sólo saldrá en el log los mensajes tipo texto
            if cid > 0:
                mensaje = str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
            else:
                mensaje = str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text 
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print mensaje
           

 
bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba

# Comprueba la privacidad sobre el uso de comandos
def autorizacion(user_id):
    return open('all_people.txt').read().rstrip() == 'true' or user_id in ADMIN

#############################################
#Funciones

# Reconoce el comando y llama a la función adecuada
@bot.message_handler(func=lambda msg:msg.text.encode("utf-8"))
def commands(m):
    if autorizacion(m.from_user.id):
        if '!pole' in m.text:
            command_pole(m)
        elif '!insultar' in m.text:
            command_insultar(m)
        elif '!clasificacion'in m.text:
            command_clasificacion(m)
        elif '!censo'in m.text:
            command_censo(m)
        elif '!hilo'in m.text:
            command_hilo(m)
        elif '!getcommands'in m.text:
            command_get_commands(m)
        elif '!setcommands'in m.text:
            command_set_commands(m)
        elif '!about' in m.text:
            command_about(m)



# Mensaje para dar la bienvenida
@bot.message_handler(content_types=['new_chat_participant'])
def bienvenido(m):
    with open('bienvenido.txt') as file:  
        mensaje = 'Bienvenido @' + m.new_chat_participant.username + '!! ' + file.read()
        bot.send_message(m.chat.id, mensaje.rstrip())



# Mensaje cuando alguien abandona el grupo
@bot.message_handler(content_types=['left_chat_participant'])
def despedida(m):
    mensaje = 'Dep, siempre saludaba'
    bot.send_message(m.chat.id, mensaje)



# Comando /pole - GRUPOS
def command_pole(m):
    if autorizacion(m.from_user.id):
        if m.chat.type == 'group' or m.chat.type == 'supergroup':
            x = datetime.datetime.now()
            hora = x.hour
            minutos = x.minute
            tiempo = str(hora) + ':' + str(minutos)
            if tiempo == HORA_POLE:
                bot.send_message(m.chat.id, 'Es la pole' + m.text)



#Comando /insultar - GRUPOS
def command_insultar(m): 
    if autorizacion(m.from_user.id):
        if m.chat.type == 'group' or m.chat.type == 'supergroup': 
            frases = {
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
                14:"Eres más tonto que cagar de pie"
            }
            
            insultado = m.text[10:]
        
            if insultado == '':                                                 # no hay persona a la que insultar
                mensaje = 'Pero dime a quién insulto, pedazo de inútil'
                bot.reply_to(m, mensaje)                                        # respondemos citando al mensaje
            else:
                if insultado == 'supremoh' or insultado == '@supremoh':         # no insulta a su creador
                    mensaje = 'Con @supremoh no, joputa, que te reviento'
                    bot.reply_to(m, mensaje)
                else:
                    if insultado[0] != '@':                                         # se ha añadidido @
                        mensaje = frases[random.randrange(len(frases))] + ' @' + insultado
                    else:                                                                   
                        mensaje = frases[random.randrange(len(frases))] + ' ' + insultado
                    bot.send_message(m.chat.id, mensaje)                            # respondemos usando el id



# Comando /clasificacion - ABIERTO
def command_clasificacion(m):
    if autorizacion(m.from_user.id):
        with open('clasificacion.txt') as file:
            mensaje = file.read()
            bot.send_message(m.chat.id, mensaje)



# Comando /censo - ABIERTO
def command_censo(m):
    if autorizacion(m.from_user.id):
        url = 'https://docs.google.com/spreadsheets/d/1WgdK9EPZhY6c15MFxixIz4IFpA_gxgwOyTwtfkT8xeo/edit#gid=0'
        bot.send_message(m.chat.id, '||| Listado de jugadores |||\n\n' + url)



# Comando /hilo - ABIERTO
def command_hilo(m):
    if autorizacion(m.from_user.id):
        url = 'http://www.forocoches.com/foro/showthread.php?p=220974491'
        bot.send_message(m.chat.id, '||| Hilo en FC |||\n\n' + url)



# Comando /getcommands - ADMIN
def command_get_commands(m):
    if m.from_user.id in ADMIN:
        bot.send_message(m.chat.id, open('all_people.txt').read().strip())



# Comando /setcommands - ADMIN
def command_set_commands(m):
    if m.from_user.id in ADMIN:
        flag = m.text[13:].strip()
        if flag == '':
            flag = 'false'
            
        with open('all_people.txt', 'w') as file:
            file.write(flag)
            bot.send_message(m.chat.id, 'Enabled commands? ' + flag)



# Comando /creditos - ABIERTO
def command_about(m):
    if autorizacion(m.from_user.id):
        bot.send_message(m.chat.id, 'Información acerca de la liga forocochera del PES6.\n\nBot creado por @supremoh para la FFPA.')

    
    
#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.