# -*- coding: utf-8 -*-
# @Author: gmm96
# @Date:   2016-03-22 01:50:50
# @Last Modified by:   gmm96
# @Last Modified time: 2016-03-22 02:56:32


import json
import sys
sys.path.append("/home/supremoh/telegramBot/workspace/")


##
## @brief  Reads a file and returns its content 
##
## @param  type     File type
## @param  file_path     Path to file
## 
## @return  The content of the specified file
##

def read_file(type, file_path):
   with open(file_path) as __file:
      if type == 'reg':
         return __file.read()
      elif type == 'json':
         return json.load(__file)



##
## @brief  Write some info in file
##
## @param  type     File type
## @param  file_path     Path to file
## @param  info_to_save     Info to save in file
##

def write_file(type, file_path, info_to_save):
   with open(file_path, 'w') as __file:
      if type == 'reg':
         __file.write(info_to_save)
      elif type == 'json':
         json.dump(info_to_save, __file)
