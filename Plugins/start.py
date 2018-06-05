# -*- coding: utf-8 -*-
markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
markups.row('💫 گروه آزمایشی','ارتباط باما 📬')

@bot.message_handler(commands=['start'])
def start(m):
 if 'private' in m.chat.type:
   bot.reply_to(m,starttext,reply_markup=markups)
   
@bot.message_handler(func=lambda m: m.text == "💫 گروه آزمایشی")
def free(m):
  if redis.get('free'+str(m.from_user.id)):
   bot.reply_to(m,'شما فقط یک بار میتوانید گروه آزمایشی دریافت کنید')
  else:
    bot.reply_to(m,'لطفا آیدی گروه خود را ارسال کنید 🌟\nشما میتوانید برای گرفتن آیدی من را در گروه اضافه کنید')
    bot.register_next_step_handler(m,freegp)
	
@bot.message_handler(func=lambda m: m.text == "ارتباط باما 📬")
def feedback(m):
    bot.reply_to(m,'اگر نظر و یا سوالی دارید ارسال کنید 🔻')
    bot.register_next_step_handler(m,support)
	
def support(m):
    bot.forward_message(sup,m.chat.id,m.message_id)
    bot.reply_to(m,'ارسال شد 👍',reply_markup=markups)
	
def freegp(m):
   redis.setex('expire'+str(m.text),'86400',True)
   bot.reply_to(m,'هورا 🎉\nگروه شما ۱ روز شارژ شد .\nحالا میتوانید ربات را برای آزمایش در گروه خود اضافه کنید 🎈',reply_markup=markups)
   redis.set('free'+str(m.from_user.id),True)
   
#Start
