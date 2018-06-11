
# -*- coding: utf-8 -*-

@bot.message_handler(func=lambda m: m.text.startswith("#Gift"))
def giftcard(m):
  if is_mod(m.chat.id,m.from_user
id):
     card = m.text.replace("#Gift","")
     if not redis.get(card):
        bot.reply_to(m,"گیفت کارد موجود نیست و یا باطل شده است 🚫")
     else:
       day = redis.get(card)
       tes = int(60) * int(60) * int(24) * int(day)
       ex = redis.ttl("expire"+str(m.chat.id))
       pes = int(ex) + int(tes)
       redis.delete(card)
       redis.setex("expire"+str(m.chat.id),pes,True)
       bot.reply_to(m,"هورا 🎉\n{} روز به شارژ‌گروه شما افزوده شد😎".format(day))
       bot.send_message(sup,'گیفت کارد توسط گروه {} باطل شد'.format(m.chat.id))

@bot.message_handler(func=lambda m: m.text.startswith("کارت"))
def creategift(m):
   if is_sudo(m.from_user.id):
     num = random.randint(1,9999999999999999)
     day = m.text.split()[1]
     redis.set(num,day)
     bot.reply_to(m,"گیفت کار با شماره \n {} ساخته شد \nروش استفاده :\n#Gift(کد)".format(num))
