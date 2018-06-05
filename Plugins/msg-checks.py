# -*- coding: utf-8 -*-

@bot.message_handler(content_types=['new_chat_members'])
def join(m):
     if str(m.new_chat_member.id) == str(botid):
       if is_sudo(m.from_user.id):
        bot.reply_to(m,'ربات افزوده شد ☂️\nلطفا ربات را در گروه روشن کنید 🔹')
       else:
        if not redis.get('expire'+str(m.chat.id)):
          bot.reply_to(m,'لطفا اول گروه خود را شارژ کنید ♦️\nایدی گروه : {}'.format(m.chat.id))
          bot.leave_chat(m.chat.id)
        else:
          bot.reply_to(m,'اسپید استار فعال شد 💫')
          redis.sadd('groups',m.chat.id)
			   
@bot.message_handler(content_types=['text', 'photo','video','video_note','audio','voice','document','sticker','contact','location','forward'])
def check_pm(m):
 if m.chat.type == 'supergroup':
   if redis.sismember('groups',m.chat.id):
     if not redis.get('expire'+str(m.chat.id)):
      bot.reply_to(m,'🔴 اعتبار گروه به پایان رسیده است 🔴')
      redis.srem('groups',m.chat.id)
      bot.leave_chat(m.chat.id)
     else:
      check(m)

def check(m):
 if not is_mod(m.chat.id,m.from_user.id):
  redis.sadd(m.content_type,m.message_id) 
  if m.chat.type == 'supergroup':
   if redis.sismember('groups',m.chat.id):
    try:
     flood_max = str(redis.get('floodmax'+str(m.chat.id)) or 3)
     flood_time = str(redis.get('floodtime'+str(m.chat.id)) or 2)
     post_count = str(redis.get("FloodCount"+str(m.chat.id)+str(m.from_user.id)) or 0)
     t = int(post_count) + int(1)
     redis.setex("FloodCount{}{}".format(m.chat.id,m.from_user.id),flood_time,t)
     gp = m.chat.id
     uid = m.from_user.id
     mid = m.message_id
     if m.sticker and redis.get('sticker'+str(gp)):
      bot.delete_message(gp,mid)
     if m.photo and redis.get('photo'+str(gp)):
      bot.delete_message(gp,mid)
     if m.video and redis.get('video'+str(gp)):
      bot.delete_message(gp,mid)
     if m.audio and redis.get('audio'+str(gp)):
      bot.delete_message(gp,mid)
     if m.voice and redis.get('voice'+str(gp)):
      bot.delete_message(gp,mid)
     if m.document and redis.get('gif'+str(gp)):
      bot.delete_message(gp,mid)
     if m.video_note and redis.get('videonote'+str(gp)):
      bot.delete_message(gp,mid)
     if m.contact and redis.get('contact'+str(gp)):
      bot.delete_message(gp,mid)
     if m.text and redis.get('text'+str(gp)):
      bot.delete_message(gp,mid)
     if m.forward_from or m.forward_from_chat and redis.get('fwd'+str(gp)):
      bot.delete_message(gp,mid)
     if m.text and len(m.text) > int(redis.get('len'+str(gp)) or 70) and redis.get('lens'+str(gp)):
      bot.delete_message(gp,mid)
     if redis.sismember('silents'+str(gp),uid):
      bot.delete_message(gp,mid)
     if redis.get('mutegroup'+str(gp)):
      bot.delete_message(gp,mid)
     if redis.get('link'+str(gp)):
      if re.findall("([Tt].[Mm][Ee]|[Tt][Ee][Ll][Ee][Gg][Rr][Aa][Mm].[Mm][Ee])+",str(m.caption or m.text)):
         bot.delete_message(gp,mid)
     if redis.get('web'+str(gp)):
      if re.findall("([Hh][Tt]|[Tt][Pp][Ss]://|[Cc][Oo][Mm]|[Ww][Ww][Ww]|[Ii][Rr])+",str(m.caption or m.text)):
         bot.delete_message(gp,mid)
     if redis.get('tag'+str(gp)):
      if re.findall("(#)+",str(m.caption or m.text)):
         bot.delete_message(gp,mid)
     if redis.get('username'+str(gp)):
      if re.findall("(@)+",str(m.caption or m.text)):
         bot.delete_message(gp,mid)
     if int(post_count) > int(flood_max) and redis.get('spam'+str(gp)):
       redis.delete('FloodCount{}{}'.format(gp,uid))
       bot.reply_to(m,'این کاربر به دلیل ارسال اسپم اخراج میشود☡باشد درس عبرتی برای دیگران😉')
       bot.kick_chat_member(gp,m.from_user.id)
    except:
     print('err')
  #Msg-Checks   
  
