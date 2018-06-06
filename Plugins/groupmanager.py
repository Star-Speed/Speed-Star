# -*- coding: utf-8 -*-
admint = 'این کاربر ادمینه 😶'


@bot.message_handler(func=lambda m: m.text == "تنظیمات")
def get_id(m):
  if is_mod(m.chat.id,m.from_user.id):
   text = '''
#تنظیمات _سوپرگروه شما_:

#اطلاعات:
>_آیدی شما_ : *{}*
>_آیدی گروه_ : *{}*
'''
   bot.reply_to(m,text.format(m.from_user.id,m.chat.id),parse_mode='markdown',reply_markup=panel_locks(m.chat.id))

@bot.message_handler(func=lambda m: m.text == "راهنما")
def help(m):
   if is_mod(m.chat.id,m.from_user.id):
    bot.reply_to(m,helpgp)
	
@bot.message_handler(func=lambda m: m.text.startswith("حذف"))
def delmsg(m):
 try:
   if is_mod(m.chat.id,m.from_user.id):
    if int(m.text.split()[1]) > int(500):
     bot.reply_to(m,'حدااکثر تعداد 500 تا است ⚡️')	
    else:
       for x in range(int(m.text.split()[1])):
                try:
                    bot.delete_message(m.chat.id, m.message_id - x)
                except:
                    pass 
       bot.send_message(m.chat.id,'{} پیام حذف شد'.format(m.text.split()[1]))
 except:
  pass 
  
@bot.message_handler(func=lambda m: m.text == "اعتبار")
def sharj(m):
   if is_mod(m.chat.id,m.from_user.id):
      t = redis.ttl('expire'+str(m.chat.id))
      byear = t % 31536000
      month = int(byear) / int(2592000)
      bmonth = int(byear) % int(2592000)
      day = int(bmonth) / int(86400)
      bday = int(bmonth) % int(86400)
      hours = int(bday) / int(3600)
      bhours = int(bday) % int(3600)
      min = int(bhours) / int(60)
      sec = int(bhours) % int(60)
      bot.reply_to(m,'گروه [{} ماه] و [{} روز] و [{} ساعت] و [{} دقیقه] و [{} ثانیه] اعتبار دارد 📅'.format(month,day,hours,min,sec))
	 
@bot.message_handler(func=lambda m: m.text == "بستن گروه" or m.text == "بازکردن گروه")
def mute_gp(m):
 try:
  if is_mod(m.chat.id,m.from_user.id):
   if str(m.text.split()[0]) == str('بستن'):
    redis.set('mutegroup'+str(m.chat.id),True) 
    bot.reply_to(m,'گروه در حال قفل قرار گرفت 🔇\n#توجه_هر_پیامی_ارسال_بشه_حذف_میکنم 😁')	
   if str(m.text.split()[0]) == str('بازکردن'):
    redis.delete('mutegroup'+str(m.chat.id)) 
    bot.reply_to(m,'گروه در حال باز قرار گرفت 🔊\n#توجه_هر_پیامی_ارسال_بشه_حذف_نمیکنم 😁')
 except Exception as e:
   print e
	
@bot.message_handler(func=lambda m: m.text == "بیصدا")
def silentuser(m):
 try:
   if is_mod(m.chat.id,m.from_user.id):
	if m.reply_to_message:
          ids = m.reply_to_message.from_user.id
          name = m.reply_to_message.from_user.first_name
          if is_mod(m.chat.id,ids):
          	bot.reply_to(m, admint)
          else:
             bot.reply_to(m, 'کاربر از الان به بعد نمیتونه تایپ کنه 🤐')
             redis.sadd('silents'+str(m.chat.id),name)
             bot.restrict_chat_member(m.chat.id, ids, until_date=0,
                 can_send_messages=False, 
                 can_send_other_messages=False)
 except Exception as e:
   print e
   
@bot.message_handler(func=lambda m: m.text == "باصدا")
def unsilentuser(m):
 try:
   if is_mod(m.chat.id,m.from_user.id):
	if m.reply_to_message:
          ids = m.reply_to_message.from_user.id
          name = m.reply_to_message.from_user.first_name
          if is_mod(m.chat.id,ids):
          	bot.reply_to(m, admint)
          else:
             bot.reply_to(m, 'کاربر ازاد شد 🤗')
             redis.srem('silents'+str(m.chat.id),name)
             bot.restrict_chat_member(m.chat.id, ids, until_date=0,
                 can_send_messages=True, 
                 can_send_other_messages=True)
 except Exception as e:
   print e
   
@bot.message_handler(func=lambda m: m.text == "لیست سکوت")
def silentlist(m):
 try:
     if is_mod(m.chat.id,m.from_user.id):
           if redis.scard('silents'+str(m.chat.id)) == int(0):
             bot.reply_to(m, 'اول یکیو خفه کن خو 😐')
           else:
              text = 'لیست افراد ساکت شده 🤐:\n'
              for all in redis.smembers('silents'+str(m.chat.id)):
                text += '{}\n'.format(all)
              bot.reply_to(m,text)
 except:
   print e
   
@bot.message_handler(func=lambda m: m.text.startswith("تنظیم اسپم"))
def setflood(m):
 try:
      if is_mod(m.chat.id,m.from_user.id):
          number = m.text.split()[2]
          if number:
           if number.isdigit(): 
            if int(number) > int(2) and int(number) < int(21):
               redis.set('floodmax'+str(m.chat.id),number)
               bot.reply_to(m,'حدااکثر تعداد اسپم تغییر کرد به : {} 🔄'.format(number))
            else:
               bot.reply_to(m,' عدد باید بین ۳ تا ۲۰ باشه کسکم 🤷‍♂')
 except:
  print(m)
  
@bot.message_handler(func=lambda m: m.text.startswith("تنظیم زمان"))
def setfloodtime(m):
 try:
      if is_mod(m.chat.id,m.from_user.id):
          number = m.text.split()[2]
          if number:
           if number.isdigit(): 
            if int(number) > int(1) and int(number) < int(10):
               redis.set('floodtime'+str(m.chat.id),number)
               bot.reply_to(m,'حدااکثر زمان ارسال پیام تغییر کرد به : {} 🔄 '.format(number))
            else:
               bot.reply_to(m,' عدد باید بین ۳ تا ۲۰ باشه جیگَلم 🤷‍♂')
 except:
  print(m)
   
@bot.message_handler(func=lambda m: m.text.startswith("فیلتر"))
def filter(m):
 try:
     text = m.text.replace('فیلتر ','')
     if is_mod(m.chat.id,m.from_user.id):
      if redis.sismember('filters'+str(m.chat.id),text):
       bot.reply_to(m,'این کلمه در لیست فیلتر موجود بود ‼️')
      else:
       redis.sadd('filters'+str(m.chat.id),text)
       bot.reply_to(m,'استفاده از کلمه [{}] ممنوع شد 🔞'.format(text))
 except Exception as e:
   print e
   
@bot.message_handler(func=lambda m: m.text.startswith("ازاد"))
def filter(m):
 try:
     text = m.text.replace('ازاد ','')
     if is_mod(m.chat.id,m.from_user.id):
       redis.srem('filters'+str(m.chat.id),text)
       bot.reply_to(m,'استفاده از کلمه [{}] آزاد شد ✅'.format(text))
 except Exception as e:
   print e
   
@bot.message_handler(func=lambda m: m.text == "لیست فیلتر")
def filterlist(m):
 try:
     if is_mod(m.chat.id,m.from_user.id):
           if redis.scard('filters'+str(m.chat.id)) == int(0):
             bot.reply_to(m, 'اول یک کلمه رو فیلتر کن 🤕')
           else:
              text = 'لیست کلمات ممنوع شده 📑:\n'
              for all in redis.smembers('filters'+str(m.chat.id)):
                text += '{}\n'.format(all)
              bot.reply_to(m,text)
 except:
   print e
		
@bot.message_handler(func=lambda m: m.text == "ترقیع")
def demote(m):
 try:
   if is_cr(m.chat.id,m.from_user.id):
    if m.reply_to_message:
     ids = m.reply_to_message.from_user.id
     if is_mod(m.chat.id,ids):
      bot.reply_to(m, 'این کاربر خودش ادمینه پس 💩 نخور 😌')
     else:
       bot.reply_to(m, '👑 مقام کاربر ارتقا یافت به مدیریت(ربات).')
       redis.sadd('promotes'+str(m.chat.id),ids)
 except Exception as e:
   print e
   
@bot.message_handler(func=lambda m: m.text == "تنزل")
def demote(m):
 try:
   if is_cr(m.chat.id,m.from_user.id):
    if m.reply_to_message:
     ids = m.reply_to_message.from_user.id
     if not is_mod(m.chat.id,ids):
      bot.reply_to(m, 'این کاربر ادمین نیست پس 💩 نخور 😌')
     else:
       bot.reply_to(m, '🎈 مقام کاربر به پشم ارتقا یافت .')
       redis.srem('promotes'+str(m.chat.id),ids)
 except Exception as e:
   print e
   
@bot.message_handler(func=lambda m: m.text.startswith("تنظیم"))
def setlink(m):
  if is_mod(m.chat.id,m.from_user.id):
   if m.text.split()[1] == 'لینک':
    link = m.text.replace('تنظیم لینک ','')
    redis.set('gplink'+str(m.chat.id),link)
    bot.reply_to(m,'📜 - لینک گروه تنظیم شد به : {}'.format(link))
   if m.text.split()[1] == 'قوانین':
    rules = m.text.replace('تنظیم قوانین','')
    redis.set('rules'+str(m.chat.id),rules)
    bot.reply_to(m,'قوانین گروه تنظیم شد 📋\n\n📍قوانین : {}'.format(rules))	
   if m.text.split()[1] == 'توضیحات':
      if not is_mod(m.chat.id,botid) :
       bot.reply_to(m,"عجیجم تا منو ادمین نکنی نمیتونم توضیحاتو تغییر بدم🍌")
      else:
        text = m.text.replace('تنظیم توضیحات ', '')
        bot.set_chat_description(m.chat.id,text)
        bot.send_message(m.chat.id, 'توضیحات گروه تنطیم شد 💭')
   if m.text.split()[1] == 'نام':
     text = m.text.replace('تنظیم نام ', '')
     bot.set_chat_title(m.chat.id, text)
     bot.reply_to(m,'نام گروه تنظیم شد به 🚶 {}'.format(text))
   if m.text.split()[1] == 'عکس':
     if m.reply_to_message.photo:
       fileid = m.reply_to_message.photo[-1].file_id
       download_file(fileid,'./data/{}.jpg'.format(m.chat.id))
       bot.set_chat_photo(m.chat.id, open('./data/{}.jpg'.format(m.chat.id), 'rb'))
       bot.reply_to(m,'عکس جدیدی برای گروه تنظیم شد 🌄')
   if m.text.split()[1] == 'سنجاق':
    if m.reply_to_message:
      bot.pin_chat_message(m.chat.id, m.reply_to_message.message_id)
      bot.reply_to(m,'پیام جدید سنجاق شد 📌')
   if m.text.split()[1] == 'کاراکتر':
     num = m.text.split()[2]
     if num.isdigit(): 
       redis.set('len'+str(m.chat.id),num)
       bot.reply_to(m,'حدااکثر تعداد کاراکتر در جمله به : {} تنظیم شد 📠'.format(num))
@bot.message_handler(func=lambda m: m.text == "قوانین")
def getrules(m):
     rules = redis.get('rules'+str(m.chat.id))
     if not rules:
      bot.reply_to(m,'هیچ قوانین برای گروه تنظیم نشده است 📁\nبا دستور [تنظیم قوانین ****] قوانین گروه را تنظیم کنید 📝')
     else:
      bot.reply_to(m,rules)
	  
	  
@bot.message_handler(func=lambda m: m.text == "لینک")
def getlink(m):
   if is_mod(m.chat.id,m.from_user.id):
     link = (redis.get('gplink'+str(m.chat.id)) or bot.export_chat_invite_link(m.chat.id))
     bot.reply_to(m,'[برای ورود به گروه {} کلیک کنید 🔅]({})'.format(m.chat.title,link),parse_mode='Markdown')

@bot.message_handler(func=lambda m: m.text == "اخراج")
def kick(m):
 try:
  if is_mod(m.chat.id,m.from_user.id):
   if m.reply_to_message:
     ids = m.reply_to_message.from_user.id
     name = m.reply_to_message.from_user.first_name
     if is_mod(m.chat.id,ids):
      bot.reply_to(m, admint)
     else:
      bot.reply_to(m,'کاربر [{}](tg://user?id={}) شوت شد بیرون 👟'.format(name,ids),parse_mode='markdown')
      bot.kick_chat_member(m.chat.id,ids)
 except Exception as e:
   print e
   
#Group-Manager

