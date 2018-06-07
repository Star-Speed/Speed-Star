# -*- coding: utf-8 -*-
markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
markups.row('💫 گروه آزمایشی','ارتباط باما 📬')
markups.row('❓راهنما')

markuphelp = types.ReplyKeyboardMarkup(resize_keyboard=True)
markuphelp.row('👥 دستورات گروه','👑 دستورات سودو')
markuphelp.row('🔙 برگشت')

markupb = types.ReplyKeyboardMarkup(resize_keyboard=True)
markupb.row('🔙 برگشت')

@bot.message_handler(func=lambda m: m.text == "/start" or m.text == '🔙 برگشت' and not redis.get('ban'+str(m.from_user.id)))
def start(m):
 if 'private' in m.chat.type:
   antiflood(m)
   redis.sadd('mbr',m.from_user.id)
   bot.reply_to(m,starttext,reply_markup=markups,disable_web_page_preview=True)
   
@bot.message_handler(func=lambda m: m.text == "❓راهنما" and not redis.get('ban'+str(m.from_user.id)))
def helps(m):
    antiflood(m)
    bot.reply_to(m,'لطفا یک گزینه را انتخاب کنید ❣️',reply_markup=markuphelp)
	
@bot.message_handler(func=lambda m: m.text == "👥 دستورات گروه" and not redis.get('ban'+str(m.from_user.id)))
def hgp(m):
    antiflood(m)
    bot.reply_to(m,helpgp)

@bot.message_handler(func=lambda m: m.text == "👑 دستورات سودو" and not redis.get('ban'+str(m.from_user.id)))
def hsudo(m):
    antiflood(m)
    bot.reply_to(m,sudohelp)
	
@bot.message_handler(func=lambda m: m.text == "💫 گروه آزمایشی" and not redis.get('ban'+str(m.from_user.id)))
def free(m):
  antiflood(m)
  if redis.get('free'+str(m.from_user.id)):
   bot.reply_to(m,'شما فقط یک بار میتوانید گروه آزمایشی دریافت کنید')
  else:
    bot.reply_to(m,'لطفا آیدی گروه خود را ارسال کنید 🌟\nشما میتوانید برای گرفتن آیدی من را در گروه اضافه کنید',reply_markup=markupb)
    bot.register_next_step_handler(m,freegp)
	
@bot.message_handler(func=lambda m: m.text == "ارتباط باما 📬" and not redis.get('ban'+str(m.from_user.id)))
def feedback(m):
    antiflood(m)
    bot.reply_to(m,'اگر نظر و یا سوالی دارید ارسال کنید 🔻',reply_markup=markupb)
    bot.register_next_step_handler(m,support)
	
def support(m):
  if m.text == '🔙 برگشت':
   bot.reply_to(m,'منو اصلی',reply_markup=markups)
  else:
    bot.forward_message(sup,m.chat.id,m.message_id)
    bot.reply_to(m,'ارسال شد 👍',reply_markup=markups)
	
def freegp(m):
  if m.text == '🔙 برگشت':
   bot.reply_to(m,'منو اصلی',reply_markup=markups)
  else:
   redis.setex('expire'+str(m.text),'86400',True)
   bot.reply_to(m,'هورا 🎉\nگروه شما ۱ روز شارژ شد .\nحالا میتوانید ربات را برای آزمایش در گروه خود اضافه کنید 🎈',reply_markup=markups)
   redis.set('free'+str(m.from_user.id),True)
   
#Start
