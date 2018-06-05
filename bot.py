#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import sys
import redis
import os
import re
from threading import Thread
import time
import datetime
import jdatetime
from threading import Timer
import random
from random import randint as rand
import urllib
import requests
import json
from telebot import types
from time import sleep
reload(sys)
session = requests.session()
import math
sys.setdefaultencoding("utf-8")
#----------------------------
execfile("config.py")
bot = telebot.TeleBot(Token)
botid = bot.get_me().id
redis = redis.StrictRedis(host='localhost', port=6379, db=0)

def dates():
    res = "http://irapi.ir/time/"
    opener = urllib2.build_opener()
    f = opener.open(res)
    parsed_json = json.loads(f.read())
    fadate = parsed_json["FAdate"]
    return fadate

def is_sudo(user_id):
    var = False
    if int(user_id) in sudos:
        var = True
    return var
	
def is_bot(chat_id):
    var = False
    if bot.get_chat_member(chat_id, botid).status in ["administrator"]:
        var = True
    return var
	
def is_mod(chat_id, user_id):
    var = False
    if bot.get_chat_member(chat_id, user_id).status in ["creator", "administrator"] or redis.sismember('promotes'+str(chat_id),user_id) and redis.sismember('groups',chat_id):
        var = True
    return var

def is_cr(chat_id, user_id):
    var = False
    if bot.get_chat_member(chat_id, user_id).status in ["creator"] and redis.sismember('groups',chat_id):
        var = True
    return var

def download_file(u,n):
            ret_msg = u
            file_info = bot.get_file(ret_msg) 
            downloaded_file = bot.download_file(file_info.file_path) 
            with open('{}'.format(n), 'wb') as new_file:
              new_file.write(downloaded_file)
            return downloaded_file
			
def panel_locks(gp):
        markup = types.InlineKeyboardMarkup()
        ee = '>'
        alltypes = ['lens','spam','link', 'tag','username','photo','video','audio','voice','document','sticker','text','forward','contact','mutegroup']
        typenames = {'lens':'کاراکتر','spam':'اسپم','mutegroup':'بستن گروه','link': "لینک", "tag": "تگ","username":"یوزرنیم","photo":'عکس','video':'فیلم','audio':'موزیک','voice':'صدا','document':'فایل','sticker':'استیکر','text':'متن','forward':'فوروارد','contact':'کانتکت'}  
        for i in alltypes:
          if redis.get(i+str(gp)):
            e = '[🔐]'
            callback = "unlock:" + i
          else:
            e = '[🔓]'
            callback = "lock:" + i
          markup.add(types.InlineKeyboardButton(str(ee)+str(typenames[i]),callback_data=callback),types.InlineKeyboardButton(e,callback_data=callback))
        return markup
  
for plugin in Plugins:
  try:
    execfile("Plugins/" + plugin + ".py")
    print("\033[1;36mLoading Plugin > " +"\033[0;32m" + plugin)
  except:
    print("\033[01;31mError In Loading Plugin " + plugin + "\033[0m")
    print("\033[01;31m" + os.popen("python ./Plugins/"+ plugin +".py").read() + "\033[0m")
    sys.exit()
print("\n\033[0;33mBot Is Running ...\n\033[0;33mSpeed Star\033[0m")

bot.polling(True)
