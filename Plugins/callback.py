# -*- coding: utf-8 -*-
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
      gp = call.message.chat.id
      if call.data.startswith('lock:'): 
        lock = call.data.replace('lock:','')
        redis.set(str(lock)+str(gp),True)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=panel_locks(gp))
      if call.data.startswith('unlock:'): 
        lock = call.data.replace('unlock:','')
        redis.delete(str(lock)+str(gp))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=panel_locks(gp))

#Call-Back
