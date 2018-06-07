# -*- coding: utf-8 -*-

@bot.message_handler(func=lambda m: m.text == "پلاگین")
def getplug(m):
 if is_sudo(m.from_user.id):
       bot.reply_to(m,'📁 پلاگین های ربات اسپید استار:\n📍برای روشن/خاموش کردن پلاگین روی پلاگین مورد نظر کلیک کنید :',reply_markup=plugs())


@bot.message_handler(func=lambda m: m.text == "افزودن پلاگین")
def addplug(m):
    if is_sudo(m.from_user.id):
       if m.reply_to_message.document:
        if m.reply_to_message.document.file_name.endswith(".py"):
          bot.reply_to(m,"پلاگین افزوده شد ✅")
          download_file(m.reply_to_message.document.file_id,"./Plugins/{}".format(m.reply_to_message.document.file_name))
