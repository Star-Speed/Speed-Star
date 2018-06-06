# -*- coding: utf-8 -*-

@bot.message_handler(func=lambda m: m.text.startswith("اخطار"))
def warn(m):
 try:
  if is_mod(m.chat.id,m.from_user.id):
   if m.reply_to_message:
    ids = m.reply_to_message.from_user.id
    name = m.reply_to_message.from_user.first_name
    if is_mod(m.chat.id,ids):
      bot.reply_to(m, 'مدیره کسگم')
    else:
     if m.text.split()[1] == "+":
          redis.hincrby("warn",ids,1)
          card = str(redis.hget("warn",ids)  or 0)
          if int(card) == int(4):
             bot.kick_chat_member(m.chat.id, ids)
             bot.send_message(m.chat.id, 'کاربر به علت اخطار های پی در پی از گروه اخراج شد ❗️\nرعایت قوانین گروه امری الزامیست ⛔️')
             redis.hdel('warn',ids)
          else:
            c = redis.hget("warn",ids) 
            bot.reply_to(m, 'کاربر 👈 [{}] \nشما یک اخطار دریافت کردید ⛔️ \n اخطار های شما 👈 [{} از 4 اخطار ] ❗️'.format(name,c))
     if m.text.split()[1] == "-":
        if int(redis.hget("warn",ids)) == int(0):
           bot.send_message(m.chat.id, 'این کاربر هیچ اخطاری دریافت نکرده است👏')
        else:
           redis.hincrby("warn",ids,-1)
           c = redis.hget("warn",ids) 
           bot.reply_to(m, 'یک اخطار از اخطار های کاربر [{}] کم شد😉 [{}|4]'.format(name,c))
 except Exception as e:
  print(e)
