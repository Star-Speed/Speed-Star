# -*- coding: utf-8 -*-

@bot.message_handler(func=lambda m: m.text == "استیکر")
def tosticker(m):
 if is_mod(m.chat.id,m.from_user.id):
   if m.reply_to_message.photo:
        id = m.reply_to_message.photo[1].file_id
        download_file(id,'./data/{}.webp'.format(id))
        bot.send_sticker(m.chat.id,open('./data/{}.webp'.format(id)))
        os.remove('./data/{}.webp'.format(id))
        
@bot.message_handler(func=lambda m: m.text == "عکس")
def tophoto(m):
 if is_mod(m.chat.id,m.from_user.id):
   if m.reply_to_message.sticker:
        id = m.reply_to_message.sticker.file_id
        download_file(id,'./data/{}.png'.format(id))
        bot.send_photo(m.chat.id,open('./data/{}.png'.format(id)))
        os.remove('./data/{}.png'.format(id))
