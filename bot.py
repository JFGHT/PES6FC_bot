# -*- coding: utf-8 -*-
 
import telebot              # Librería de la API del bot.
from telebot import types   # Tipos para la API del bot.
import time                 # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
from time import sleep
from threading import Thread
import json
import sys

reload(sys)                           # python 2
sys.setdefaultencoding("utf-8")       #


#Variables globales
#############################################
TOKEN = '196817759:AAGPd3ZCCnByvXjUE-MHZRD6ZIGtR9uWr0M' # token del bot
ADMIN = [6216877]
GRUPOS = [-30460278, -119705997]

with open('poles.json') as file:        # Leer ficheros al comienzo
    POLES = json.load(file)
with open('fechas.json') as other_file:
        FECHAS = json.load(other_file)
#############################################

# Creamos el objeto de nuestro bot
bot = telebot.TeleBot(TOKEN) 

#############################################
#Listener
# Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
def listener(messages): 
    for m in messages:
        cid = m.chat.id
        if m.content_type == 'text':
            if cid > 0:                                                                 # Conversación privada
                mensaje = str(m.chat.first_name) + " (" + str(cid) + "): " + m.text
            else:                                                                       # Grupos
                mensaje = m.from_user.username + '(' + str(m.from_user.id) + ') in "' + m.chat.title + '"[' + str(cid) + ']: ' + m.text
            # mensaje = m.from_user.username + '(' + str(m.from_user.id) + '): ' + m.text + ' : [' + str(cid) + ']'
            f = open('log.txt', 'a')
            f.write(mensaje + "\n")
            f.close()
            print(mensaje)

# Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba
bot.set_update_listener(listener)

#############################################
#Funciones

# Comprueba la privacidad sobre el uso de comandos
def autorizacion(user_id):
    return open('all_people.txt').read().rstrip() == 'true' or user_id in ADMIN



# Comprueba si m llega desde un grupo autorizado
def comprueba_grupo(m):
    return ((m.chat.type == 'group' or m.chat.type == 'supergroup') and (m.chat.id in GRUPOS))



# Devuelve la fecha en formato dd-mm-yyyy de un mensaje
def get_readable_date(unix_date):
    return datetime.datetime.fromtimestamp(unix_date).strftime('%d-%m-%Y')



# Reconoce el comando y llama a la función adecuada
@bot.message_handler(func=lambda msg:msg.text.encode("utf-8"))     # python 2
# @bot.message_handler(content_types=['text'])                        # python 3
def commands(m):
    if autorizacion(m.from_user.id):
        c = [
            '/equipos', '/pole', '/insultar', 
            '/clasificacion', '/censo', '/hilo', 
            '/getcommands', '/setcommands', '/info', 
            '/ayuda', '/nohomo', '/stats'
            ]
            
        if c[0] in m.text[:len(c[0])]:
            command_equipos(m)
        elif c[1] in m.text[:len(c[1])]:
            command_pole(m)
        elif c[2] in m.text[:len(c[2])]:
            command_insultar(m)
        elif c[3] in m.text[:len(c[3])]:
            command_clasificacion(m)
        elif c[4] in m.text[:len(c[4])]:
            command_censo(m)
        elif c[5] in m.text[:len(c[5])]:
            command_hilo(m)
        elif c[6] in m.text[:len(c[6])]:
            command_get_commands(m)
        elif c[7] in m.text[:len(c[7])]:
            command_set_commands(m)
        elif c[8] in m.text[:len(c[8])]:
            command_info(m)
        elif c[9] in m.text[:len(c[9])]:
            command_ayuda(m)
        elif c[10] in m.text[:len(c[10])]:
            command_nohomo(m)
        elif c[11] in m.text[:len(c[11])]:
            command_stats(m)
        elif 'pole' in m.text.lower():
            command_detectar_pole(m)



# Detecta la pole - GRUPOS
def command_detectar_pole(m):
    global POLES, FECHAS
    if comprueba_grupo(m):
        time = get_readable_date(m.date)
        if time not in FECHAS:
            bot.reply_to(m, 'Menudo hijo de puta, tienes unas poles del copón. De fails nada, tu das gloria. ' +
                            'Menudas poles tienes, hijo de la gran puta. Olvídate de dejarlo, potencia esa mente tan espectacular ' + 
                            'que tienes, hijo de una perra sarnosa. Qué puta envidia me das!')
    
            poleador = m.from_user.username
            FECHAS[time] = poleador
            
            if poleador in POLES:
                POLES[poleador] += 1
            else:
                POLES[poleador] = 1
            
            with open('poles.json', 'w') as file:
                json.dump(POLES, file)
            with open('fechas.json', 'w') as other_file:
                json.dump(FECHAS, other_file)



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
    global FECHAS, POLES
    if comprueba_grupo(m): 
        time = get_readable_date(m.date)
        if time in FECHAS:
            bot.send_message(m.chat.id, '||| Poleador del día |||\n\n@' + FECHAS[time])
        else: 
            bot.send_message(m.chat.id, 'A qué esperas, hijo de puta? Haz la puñetera pole de una vez.')



#Comando /insultar - GRUPOS
def command_insultar(m): 
    if comprueba_grupo(m): 
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
                if insultado[0] != '@':                                     
                    mensaje = frases[random.randrange(len(frases))] + ' @' + insultado
                else:                                                                   
                    mensaje = frases[random.randrange(len(frases))] + ' ' + insultado
                bot.send_message(m.chat.id, mensaje)                            # respondemos usando el id



# Comando /clasificacion - ABIERTO
def command_clasificacion(m):
    with open('clasificacion.txt') as file:
        mensaje = file.read()
        bot.send_message(m.chat.id, mensaje)



# Comando /censo - ABIERTO
def command_censo(m):
    url = 'https://docs.google.com/spreadsheets/d/1WgdK9EPZhY6c15MFxixIz4IFpA_gxgwOyTwtfkT8xeo/edit#gid=0'
    bot.send_message(m.chat.id, '||| Listado de jugadores |||\n\n' + url)



# Comando /hilo - ABIERTO
def command_hilo(m):
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



# Comando /stats - GRUPOS
def command_stats(m):
    global POLES
    if comprueba_grupo(m): 
        mensaje = '||| Listado de poleadores |||\n\n'
        for key,value in POLES.items():
            mensaje += '@' + key + ' - ' + str(value) + '\n'
        bot.send_message(m.chat.id, mensaje)


 
# Comando /nohomo - GRUPOS
def command_nohomo(m):
    if comprueba_grupo(m): 
        with open('nohomo.txt') as file:
            sihomo = file.read().split()
            mensaje = sihomo[random.randrange(len(sihomo))]
            bot.send_message(m.chat.id, mensaje)



# Comando /equipos - ABIERTO
def command_equipos(m):
    with open('equipos.txt') as file:
        mensaje = file.read().rstrip()
        bot.reply_to(m, mensaje)



# Comando /info - ABIERTO
def command_info(m):
    bot.send_message(m.chat.id, 'Información acerca de la liga forocochera del PES6.\n\nBot creado por @supremoh para la FFPA.')



# Comando /ayuda - ABIERTO
def command_ayuda(m):
    with open('ayuda.txt') as file:
        mensaje = file.read().rstrip()
        bot.send_message(m.chat.id, mensaje)



#############################################
#Peticiones
bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.