# -*- coding: utf-8 -*-
@bot.message_handler(func=lambda m: m.text == "روشن")
def addgp(m):
 if is_sudo(m.from_user.id) and 'supergroup' in m.chat.type:
  if not is_bot(m.chat.id):
   bot.reply_to(m,'لطفا اول ربات را ادمین گروه کنید 👤')
  else:
   if redis.sismember('groups',m.chat.id):
     bot.reply_to(m,'ربات در این گروه فعال بود 🤑')
   else:
     redis.sadd('groups',m.chat.id)
     bot.reply_to(m,'ربات در گروه فعال شد 🎉')

@bot.message_handler(func=lambda m: m.text == "خاموش")
def remgp(m):
 if is_sudo(m.from_user.id) and 'supergroup' in m.chat.type:
   if not redis.sismember('groups',m.chat.id):
     bot.reply_to(m,'ربات در این گروه فعال نیست ❌')
   else:
     bot.reply_to(m,'ربات غیرفعال شد ❗️')
     redis.srem('groups',m.chat.id)
	
@bot.message_handler(func=lambda m: m.text == "ریلود")
def reload(m):
    bot.send_message(m.chat.id, "ربات ریلود شد", parse_mode="Markdown")
    python = sys.executable
    os.execl(python, python, *sys.argv)

	
@bot.message_handler(func=lambda m: m.text == "اطلاعات")
def status(m):
  if is_sudo(m.from_user.id):
      b = ['text','photo','video','audio','voice','document','viceo_note','sticker','contact','forward','location']
      type = {'text':'متن','photo':'عکس','video':'فیلم','audio':'موزیک','voice':'صدا','document':'فایل','viceo_note':'پیام ویدئویی','sticker':'استیکر','contact':'شماره','forward':'فوردارد','location':'لوکیشن'}
      text = 'تعداد کل پیام های دریافتی 📝\n'
      x = 0
      for i in b:
       count = redis.scard(i)
       x = x + int(count)
       text += '{} : {}\n--------------\n'.format(type[i],count)
      text += '📑 تعداد کل پیام ها : '+str(x)
      text += '\n👥 تعداد کل گروه ها : '+str(redis.scard('groups'))
      bot.reply_to(m,text)
	  
	  
@bot.message_handler(func=lambda m: m.text == "فوروارد")
def fwdgp(m):
  if is_sudo(m.from_user.id):
   if m.reply_to_message:
    mid = m.reply_to_message.message_id
    x = 0
    for all in redis.smembers('groups'):
      try:
        bot.forward_message(all, m.chat.id,mid)
        x = x + 1
      except:
        redis.srem('groups',all)
    bot.reply_to(m,'پیام به {} گروه فورارد شد 💪'.format(x))

@bot.message_handler(func=lambda m: m.text == "دستورات")
def helpsudo(m):
  if is_sudo(m.from_user.id):
   bot.reply_to(m,sudohelp)

@bot.message_handler(func=lambda m: m.text == "خروج")
def leave(m):
  if is_sudo(m.from_user.id) and 'supergroup' in m.chat.type:
    bot.leave_chat(m.chat.id)
   

@bot.message_handler(func=lambda m: m.text.startswith("شارژ"))
def setexpire(m):
  try:
   if is_sudo(m.from_user.id) and 'supergroup' in m.chat.type:
    day = m.text.split()[1]
    if day.isdigit(): 
      num = int(60) * int(60) * int(24) * int(day)
      t = redis.ttl('expire'+str(m.chat.id))
      tes = int(t) + int(num)
      redis.setex('expire'+str(m.chat.id),tes,True)
      bot.reply_to(m,'گروه به مدت {} روز شارژ شد📆'.format(day))
  except:
    print('err')
    
@bot.message_handler(func=lambda m: m.text.startswith("کسر شارژ"))
def expireend(m):
  try:
   if is_sudo(m.from_user.id) and 'supergroup' in m.chat.type:
    day = m.text.split()[2]
    if day.isdigit(): 
      num = int(60) * int(60) * int(24) * int(day)
      t = redis.ttl('expire'+str(m.chat.id))
      tes = int(t) - int(num)
      redis.setex('expire'+str(m.chat.id),tes,True)
      bot.reply_to(m,'{} روز از شارژ گروه کسر شد📆'.format(day))
  except:
    print('err')
	
@bot.message_handler(func=lambda m: m.text == "اسپید" or m.text == "speed")
def speed(m):
   bot.reply_ro(m,about)

#Tools
