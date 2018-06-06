# -*- coding: utf-8 -*-
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
      gp = call.message.chat.id
      if call.data.startswith('lock:'):
       if is_mod(gp,call.from_user.id):
        lock = call.data.replace('lock:','')
        redis.set(str(lock)+str(gp),True)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=panel_locks(gp))
      if call.data.startswith('unlock:'): 
       if is_mod(gp,call.from_user.id):
        lock = call.data.replace('unlock:','')
        redis.delete(str(lock)+str(gp))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=panel_locks(gp))
      if call.data.startswith('plug:'): 
       if is_sudo(call.from_user.id):
        plug = call.data.replace('plug:','')
        if redis.get(plug):
          redis.delete(plug)
          bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=plugs())
        else:
          redis.set(plug,True)
          bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=plugs())
        python = sys.executable
        os.execl(python, python, *sys.argv)
#Call-Back
