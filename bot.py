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
import urllib2
import json
import requests
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
redis.set('tools.py',True)
redis.set('callback.py',True)
redis.set("plugins.py",True)

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

def antiflood(m):
  if not is_sudo(m.from_user.id):
    _hash = "anti_flood:user:" + str(m.from_user.id)
    max_time = 2
    max_msg = 2
    msgs = int(redis.get(_hash) or 0)
    redis.setex(_hash, max_time, int(msgs) + int(1))
    if int(msgs) >= int(max_msg):
      bot.reply_to(m,"شما به دلیل ارسال پشت سرهم پیغام، 60 ثانیه مسدود شدید 🚫")
      redis.delete(_hash)
      redis.setex('ban'+str(m.from_user.id),60,True)
	  
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
def plugs():
  markup = types.InlineKeyboardMarkup()
  for plugin in os.listdir('Plugins'):
    if redis.get(plugin):
     type = '✅'
    else:
     type = '❌'
    markup.add(types.InlineKeyboardButton('📁{} : {}'.format(plugin,type),callback_data='plug:'+str(plugin)))
  return markup
	
for plugin in os.listdir('Plugins'):
  try:
   if redis.get(plugin):
    execfile("Plugins/" + plugin)
    print("\033[1;36mLoading Plugin > " +"\033[0;32m" + plugin)
   else:
    pass
  except Exception as e:
    print("\033[01;31mError In Loading Plugin " + plugin + "\033[0m")
    print("\033[01;31m" + os.popen("python ./Plugins/"+ plugin).read() + "\033[0m")
    bot.send_message(sup,'⚠️ خطا در اجرا پلاگین {} ⚠️\n⁉️ شرح خطا : {}'.format(plugin,e))
print("\n\033[0;33mBot Is Running ...\n\033[0;33mSpeed Star\033[0m")

@bot.message_handler(content_types=['text', 'photo','video','video_note','audio','voice','document','sticker','contact','location','forward'])
def check_pm(m):
 if m.chat.type == 'supergroup':
   redis.sadd(m.content_type,m.message_id) 
   if redis.sismember('groups',m.chat.id):
     if not redis.get('expire'+str(m.chat.id)):
      bot.reply_to(m,'🔴 اعتبار گروه به پایان رسیده است 🔴')
      redis.srem('groups',m.chat.id)
      bot.leave_chat(m.chat.id)
     else:
      check(m)
 if m.chat.type == 'private':
   if m.reply_to_message.forward_from:
    if is_sudo(m.from_user.id):
     id =  m.reply_to_message.forward_from.id
     if m.text == 'مسدود':
      redis.set('ban'+str(id),True)
      bot.reply_to(m,'این کاربر دیگر قادر به استفاده از پیوی ربات نیست ❌')
     elif m.text:
      bot.send_message(id,m.text)
      bot.reply_to(m,'رفت براش')
     elif m.sticker:
      bot.send_sticker(id,m.sticker.file_id)
      bot.reply_to(m,'رفت براش')
     elif m.photo:
      bot.send_photo(id,m.photo[-1].file_id)
      bot.reply_to(m,'رفت براش')
	  
bot.polling(True)

